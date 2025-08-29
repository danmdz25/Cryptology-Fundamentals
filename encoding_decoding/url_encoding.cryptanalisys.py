import urllib.parse

with open("url_encoding.txt", "r") as f:
    texto_url = f.read()

texto_decodificado = urllib.parse.unquote(texto_url)
print(texto_decodificado)