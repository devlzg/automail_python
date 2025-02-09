import base64 # para embedar a imagem no html

# Convertendo a imagem para base64, assim podendo enviála embedada no corpo do email
with open("./assets/odonto_azul.png", "rb") as arquivo_imagem:
    img_base64 = base64.b64encode(arquivo_imagem.read()).decode("utf-8")


def conteudo_html(destinatario_nome):
    return f"""
        <html>
            <body>
                <h1>Olá!</h1>
                <p>Este é um email de teste em HTML enviado para <b>{destinatario_nome}</b> através de uma automatização feita em Python!</p>
                <img src="data:image/jpeg;base64,{img_base64}" alt="Logo da empresa" width=20% height=20%>
            </body>
        </html>
    """
