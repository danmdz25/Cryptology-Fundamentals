import hashlib 

hash_da_questao = "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"#160 bits - sha1
palavras = ["cryptography", "hello", "world", "test", "cryptanalysis","cryptographic"]
for palavra in palavras:
    hash_calculado = hashlib.sha1(palavra.encode()).hexdigest()

    if hash_calculado == hash_da_questao:
        print(f"A palavra correta é: {palavra}")
        break
    else:
        print("A palavra não corresponde ao hash fornecido.")
        print(f"Hash calculado: {hash_calculado}")