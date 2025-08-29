
#ascii 
ascii=[83,116,97,114,114,121,78,105,103,104,116,86,97,110,71,111,103,104]
texto_final=''

for i in ascii:
    texto_decodificado = chr(i)
    texto_final+=texto_decodificado

print(texto_final)