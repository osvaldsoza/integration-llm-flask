<<<<<<< HEAD
# Flask LLM Integration

Este projeto demonstra como integrar um modelo de linguagem (LLM) usando Flask.

## Estrutura do Projeto

project-root/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── templates/
│ └── index.html
└── venv/

## Pré-requisitos

- Python 3.x
- pip3

## Configuração

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/osvaldsoza/integration-llm-flask.git
   cd integration-llm-flask
   
## Criar e Ativar o Ambiente Virtual

1. **Execute o seguinte comando,no ``windows, macOS e Linux``, para criar o ambiente virtual:**

   ```bash
   python3 -m venv venv

2. **Execute o seguinte comando, no ``macOS e Linux``, para ativar o ambiente virtual:**

   ```bash
   source venv/bin/activate
 
3. **Execute o seguinte comando, no ``windows``, para ativar o ambiente virtual:**

   ```bash
   .\venv\Scripts\activate

## Instalar as Dependências

Para instalar as dependências listadas no arquivo `requirements.txt`, execute o seguinte comando:

   ```bash
    pip3 install -r requirements.txt
   ```
   
## Gerar a Chave de API da OpenAI

Para usar a OpenAI API, você precisa de uma chave de API válida. Siga os passos abaixo para gerar sua chave de API:

1. Acesse o [site da OpenAI](https://platform.openai.com/api-keys) para gerar sua chave de API:

   - Faça login ou crie uma conta na OpenAI, se ainda não tiver uma.
   - Navegue até a seção de chaves de API.
   - Clique em "Create new secret key" para gerar uma nova chave de API.
   - Copie a chave gerada.

2. **Importante:** Verifique se há créditos disponíveis na sua conta da OpenAI para usar a API. A execução de solicitações para o modelo de linguagem pode consumir créditos. Certifique-se de que sua conta esteja configurada com créditos suficientes para evitar interrupções no uso da API.

3. Configure a variável de ambiente no arquivo `.env` na raiz do projeto:

   ```plaintext
   OPENAI_API_KEY=sua-chave-api-aqui
=======
# Integration LLM Flask
## source venv/bin/activate
## pip install flask openai==0.28 python-dotenv

>>>>>>> a8d7af3a970c454b8e17ecd2899812158702d18f
