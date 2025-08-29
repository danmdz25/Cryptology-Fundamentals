import hashlib

with open('criptografia/rockyou.txt','r', encoding='latin-1') as f:
    word_list = f.read().splitlines()

with open('criptografia/sha1-hash.txt','r') as f:
    hash_to_crack=f.read().strip()


for i in word_list:
    hashed_word = hashlib.sha1(i.encode()).hexdigest()
    if hashed_word == hash_to_crack:
        print(f"Senha encontrada: {i}")
        break