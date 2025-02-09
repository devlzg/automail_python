import base64 # para embedar a imagem no html

# Convertendo a imagem para base64, assim podendo enviála embedada no corpo do email
# Isso só funciona em alguns provedores de email, no outlook por exemplo, já no gmail a imagem precisaria estar hospedada em algum lugar
# with open("./assets/odonto_azul.png", "rb") as arquivo_imagem:
#     img_base64 = base64.b64encode(arquivo_imagem.read()).decode("utf-8")


def conteudo_html(destinatario_nome):
    return f"""
        <html>
            <body>
                <h1>Olá!</h1>
                <p>Este é um email de teste em HTML enviado para <b>{destinatario_nome}</b> através de uma automatização feita em Python!</p>
                <img src="https://app.odontogroup.com.br/assets/media/logos/odonto_azul.png" alt="Logo da empresa" width=20% height=20%>
            </body>
        </html>
    """
