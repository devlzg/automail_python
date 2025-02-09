import os # importando funções do sistema operacional
from dotenv import load_dotenv # importando funções para o funcionamento da .env
from email.message import EmailMessage # biblioteca nativa do python
import ssl # protocolo de segurança
import smtplib # biblioteca para o envio de emails
import json # biblioteca para carregar os dados recebidos por json
from conteudo_email import conteudo_html
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

    # Criando um objeto EmailMessage e passando o conteúdo do email
    email = EmailMessage() # cria uma mensagem estruturada como um email
    email["From"] = remetente_email
    email["To"] = destinatario_email
    assunto_email = "Teste"
    email["Subject"] = assunto_email

    # Conteúdo do email em string por questões de compatibilidade
    conteudo_string = f"""
            Este é um email de teste enviado para {destinatario_nome} através de uma automatização feita em Python!
        """
    email.set_content(conteudo_string)
    
    # Conteúdo do email em html, passando o nome do destinatario para personalizar a mensagem
    email.add_alternative(conteudo_html(destinatario_nome), subtype="html")

    # anexando o PDF
    with open("./assets/anexo_exemplo.pdf", "rb") as pdf_file: # rb pois pdf tem dados binarios e nao é somente texto
        dados_pdf = pdf_file.read()
    email.add_attachment(dados_pdf, maintype="application", subtype="pdf", filename="anexo_exemplo.pdf")

    # Cria um contexto SSL seguro (criptografia).
    context = ssl.create_default_context() 

    # Envia o email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(remetente_email, senha_email)
        smtp.sendmail(remetente_email, destinatario_email, email.as_string())

    print("Email enviado com sucesso!") # remover isso depois
