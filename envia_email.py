import os # importando funções do sistema operacional
from dotenv import load_dotenv # importando funções para o funcionamento da .env
from email.message import EmailMessage # biblioteca nativa do python
import ssl # protocolo de segurança
import smtplib # biblioteca para o envio de emails
import json # biblioteca para carregar os dados recebidos por json
load_dotenv()

def envia_email(dados_json):

    # Carregando dados do json
    with open(dados_json, 'r', encoding='utf-8') as f: # traz os dados do json para a variável "dados"
        dados = json.load(f)

    # Remetente e destinatário
    remetente_email = os.getenv("EMAIL") # pegando meu email e senha da variável de ambiente
    senha_email = os.getenv("SENHA_EMAIL")
    destinatario_email = dados["email"]
    destinatario_nome = dados["nome"]

    # Conteúdo do email
    assunto_email = "Teste"
    body = f"""
        Este é um email de teste enviado para {destinatario_nome} através de uma automatização feita em Python!
    """

    # Criando um objeto EmailMessage e passando o conteúdo do email
    email = EmailMessage() # cria uma mensagem estruturada como um email
    email["From"] = remetente_email
    email["To"] = destinatario_email
    email["Subject"] = assunto_email
    email.set_content(body)

    context = ssl.create_default_context() # cria um contexto SSL seguro (criptografia).

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(remetente_email, senha_email)
        smtp.sendmail(remetente_email, destinatario_email, email.as_string())

    print("Email enviado com sucesso!") # remover isso depois
