import base64

with open("base32.txt","r") as f:
    texto_base32 = f.read()

decoded_text = base64.b32decode(texto_base32).decode('utf-8')
print(decoded_text)