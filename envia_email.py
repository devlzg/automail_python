import os # importando funções do sistema operacional
from dotenv import load_dotenv # importando funções para o funcionamento da .env
from email.message import EmailMessage # biblioteca nativa do python
import ssl # adiciona uma camada de segurança
import smtplib # biblioteca para o envio de emails
import json # biblioteca para carregar os dados recebidos por json
load_dotenv()

# Carregando dados do json
dados_json = "./dados_email.json" # caminho para o arquivo json
with open(dados_json, 'r', encoding='utf-8') as f: # traz os dados do json para a variável "dados"
    dados = json.load(f)

# Remetente e destinatário
remetente_email = os.getenv("EMAIL")
senha_email = os.getenv("SENHA_EMAIL")
destinatario_email = dados["email"]
destinatario_nome = dados["nome"]

# Conteúdo do email
assunto_email = "Teste"
body = f"""
    Este é um email de teste enviado para {destinatario_nome} através de uma automatização feita em Python!
"""

# Criando um objeto EmailMessage e passando o conteúdo do email
email = EmailMessage()
email["From"] = remetente_email
email["To"] = destinatario_email
email["Subject"] = assunto_email
email.set_content(body) # estudar melhor sobre esse objeto

context = ssl.create_default_context() # preciso pesquisar oq isso aq faz exatamente

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp: # estudar melhor sobre essa lib
    smtp.login(remetente_email, senha_email)
    smtp.sendmail(remetente_email, destinatario_email, email.as_string())