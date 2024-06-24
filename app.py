from flask import Flask, request, render_template
import openai
import time
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_response(prompt, model="gpt-3.5-turbo", max_tokens=150, retries=3, backoff_factor=2):
    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=max_tokens,
                temperature=0.7,
            )
            return response['choices'][0]['message']['content'].strip()
        except openai.error.RateLimitError:
            if attempt < retries - 1:
                time.sleep(backoff_factor ** attempt)  # Exponential backoff
            else:
                return "Error: Rate limit exceeded. Please try again later."
        except openai.error.InvalidRequestError as e:
            return f"Invalid request: {e}"
        except Exception as e:
            return f"An error occurred: {e}"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = generate_response(prompt)
        return render_template("index.html", prompt=prompt, response=response)
    return render_template("index.html", prompt="", response="")


if __name__ == "__main__":
    app.run(debug=True)
