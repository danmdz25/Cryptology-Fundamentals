import hashlib 

hash_da_questao = "21232f297a57a5a743894a0e4a801fc3"#128 bits - md5
palavras = ["cryptography", "hello", "world", "test", "cryptanalysis","cryptographic"]
for palavra in palavras:
    hash_calculado = hashlib.md5(palavra.encode()).hexdigest()

    if hash_calculado == hash_da_questao:
        print(f"A palavra correta é: {palavra}")
        break
    else:
        print("A palavra não corresponde ao hash fornecido.")
        print(f"Hash calculado: {hash_calculado}")