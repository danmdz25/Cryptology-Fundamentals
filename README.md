# 🔐 Estudos em Criptografia e Criptoanálise
*(Scroll down for English version)*

Este repositório documenta meus estudos e práticas relacionados ao **Módulo 2: Criptografia e Criptoanálise**, com foco em técnicas de encoding/decoding e hash cracking.

---

## 📚 Conteúdo Abordado

* **Encoding e Decodificação**: Técnicas para identificar e reverter diferentes formatos de codificação de dados.
* **Hash Cracking**: Métodos práticos para descobrir senhas a partir de seus hashes, utilizando ataques de dicionário.

---

## 📦 Encoding e Decodificação

Aprendi a identificar e converter diferentes tipos de codificações para texto legível, utilizando `Python`:

* **Hexadecimal**: Conversão de strings hexadecimais para texto.
* **Binário**: Decodificação de strings binárias para caracteres ASCII.
* **Base32**: Uso do módulo `base64` para decodificação de `Base32`.
* **Quoted-Printable**: Manipulação de bytes com os módulos `quopri` e `io.BytesIO`.
* **HTML Entities**: Conversão de entidades HTML (`&lt;`, `&gt;`, etc.) para seus caracteres correspondentes.
* **UUencoding**: Decodificação de dados no formato UUencode usando o módulo `uu`.

## 🔓 Hash Cracking

Estudo prático de técnicas para descobrir senhas a partir de hashes, focando em:

* **Ataques de Dicionário**: Utilização de listas de palavras para realizar força bruta de forma mais eficiente e direcionada.
* **Wordlist `rockyou.txt`**: Emprego de uma das wordlists mais famosas e eficazes em testes de segurança para simulações realistas.
* **Algoritmos de Hash**: Análise das diferenças práticas entre os algoritmos `MD5` e `SHA1` no contexto de cracking.
* **Scripting em Python**: Desenvolvimento de scripts para automatizar o processo de cracking, incluindo as seguintes etapas:
    1.  Leitura eficiente de uma wordlist.
    2.  Geração de hash para cada palavra da lista.
    3.  Comparação do hash gerado com um hash alvo para encontrar a senha original.

## 🐍 Automação com Python

Todo o processo de análise e cracking foi automatizado com scripts `Python`, reforçando a prática em automação de tarefas de cibersegurança e análise de dados.

---
---

# 🔐 Studies in Cryptography and Cryptanalysis (English Version)

This repository documents my studies and practices related to **Module 2: Cryptography and Cryptanalysis**, focusing on encoding/decoding and hash cracking techniques.

---

## 📚 Content Covered

* **Encoding and Decoding**: Techniques for identifying and reversing different data encoding formats.
* **Hash Cracking**: Practical methods for discovering passwords from their hashes using dictionary attacks.

---

## 📦 Encoding and Decoding

I learned how to identify and convert different types of encodings to readable text using Python:

* **Hexadecimal**: Conversion of hexadecimal strings to text.
* **Binary**: Decoding binary strings to ASCII characters.
* **Base32**: Use of the base64 module for Base32 decoding.
* **Quoted-Printable**: Manipulating bytes with the `quopri` and `io.BytesIO` modules.
* **HTML Entities**: Converting HTML entities (`&lt;`, `&gt;`, etc.) to their corresponding characters.
* **UUencoding**: Decoding data in UUencode format using the `uu` module.

## 🔓 Hash Cracking

Practical study of techniques for discovering passwords from hashes, focusing on:

* **Dictionary Attacks**: Using word lists to perform brute force attacks in a more efficient and targeted manner.
* **Wordlist `rockyou.txt`**: Use of one of the most famous and effective wordlists in security testing for realistic simulations.
* **Hash Algorithms**: Analysis of the practical differences between the `MD5` and `SHA1` algorithms in the context of cracking.
* **Python Scripting**: Development of scripts to automate the cracking process, including the following steps:
1.  Efficient reading of a wordlist.
2.  Hash generation for each word in the list.
3.  Comparison of the generated hash with a target hash to find the original password.

## 🐍 Automation with Python

The entire analysis and cracking process was automated with Python scripts, reinforcing the practice of automating cybersecurity tasks and data analysis.

