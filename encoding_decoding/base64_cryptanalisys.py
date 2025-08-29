import base64

with open("base64.txt", "r") as f:
    texto_base64 = f.read()

texto_decodificado = base64.b64decode(texto_base64).decode('utf-8')
print(texto_decodificado)


