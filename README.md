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
## Identificação:

### ✳️ Hex Encoding

Codifica dados em representação hexadecimal, utilizando dígitos de 0 a 9 e letras de A a F para representar bytes.

- **Exemplo**: `"48656c6c6f"` → `"Hello"`
- **Uso**: Ferramenta comum em dumps de memória e codificação binária.

---

### 🌐 URL Encoding (Percent-Encoding)

Codifica caracteres especiais em URLs utilizando `%` seguido por dois dígitos hexadecimais.

- **Exemplo**: `"Hello World!"` → `"Hello%20World%21"`
- **Uso**: Necessária para transmitir dados seguros por URLs.

---

### 🔤 ASCII (American Standard Code for Information Interchange)

Conjunto padrão de codificação de caracteres que representa texto em computadores.

- **Exemplo**: `72 101 108 108 111` (em decimal) → `"Hello"`
- **Uso**: Base para diversas codificações modernas (UTF-8, etc.).

---

### 🔢 Binary Encoding

Representa caracteres usando sequências de 0s e 1s (bits).

- **Exemplo**: `"01001000 01100101 01101100 01101100 01101111"` → `"Hello"`
- **Uso**: Comunicação de baixo nível entre sistemas.

---

### 📦 Base64

Codifica dados binários como texto ASCII usando 64 caracteres (A-Z, a-z, 0-9, + e /).

- **Exemplo**: `"Hello"` → `"SGVsbG8="`
- **Uso**: Embutir dados binários (como imagens) em texto, por exemplo em e-mails ou JSON.

---

### 📦 Base32

Semelhante ao Base64, mas usa 32 caracteres seguros para nomes de arquivos e URLs.

- **Exemplo**: `"Hello"` → `"JBSWY3DP"`
- **Uso**: Alternativa segura ao Base64 quando se exige compatibilidade com sistemas sensíveis a caracteres especiais.

---

### 🧩 HTML Character Entities

Representa caracteres especiais em HTML com uma entidade iniciada por `&`.

- **Exemplo**: `"&lt;"` → `"<"`
- **Uso**: Prevenção de injeção de código HTML/JS (XSS).

---

### 📄 Quoted-Printable

Codificação usada em e-mails para transmitir dados binários ou caracteres especiais em texto ASCII.

- **Exemplo**: `"Hello=0AWorld"` → `"Hello\nWorld"`
- **Uso**: Usado por MIME para envio de e-mails com caracteres especiais.

---

### 📁 UUEncoding (Unix-to-Unix Encoding)

Codifica dados binários em texto para transmissão entre sistemas Unix.

- **Exemplo**: Arquivos `.uu` contendo dados codificados.
- **Uso**: Comunicação entre sistemas que não suportam dados binários diretamente.

  
---
## Conversão:

* **Hexadecimal**: Conversão de strings hexadecimais para texto, usando as funções built-in `bytes.fromhex` () e `.decode()` do python
* **Binário**: Decodificação de strings binárias para caracteres ASCII, usando as funções built-in `chr()` e `int()`.
* **Base64**: Uso do módulo `base64` para decodificação de `Base64`, usando as funções `base64.b64decode()` e `.decode()`.
* **Base32**: Uso do módulo `base64` para decodificação de `Base32`, usando as funções `base64.b64decode()` e `.decode()`.
* **Quoted-Printable**: Manipulação de bytes com os módulos `quopri` e `io.BytesIO`, usando as funções `io.BytesIO()`, `quopri.decode()`, `.decode()` e `.getvalue()`
* **HTML Entities**: Conversão de entidades HTML (`&lt;`, `&gt;`, etc.) para seus caracteres correspondentes, usando o módulo html e a função `html.unescape()`    
* **UUencoding**: Decodificação de dados no formato UUencode usando o módulo `uu`, usando as funções `io.BytesIO()`, `.getvalue()`, `.decode()` e `.encode()`

  
---

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
## Identification:

### ✳️ Hex Encoding

Encodes data in hexadecimal representation, using digits from 0 to 9 and letters from A to F to represent bytes.

- **Example**: `“48656c6c6f”` → `“Hello”`
- **Use**: Common tool in memory dumps and binary encoding.

---

### 🌐 URL Encoding (Percent-Encoding)

Encodes special characters in URLs using `%` followed by two hexadecimal digits.

- **Example**: `“Hello World!”` → `“Hello%20World%21”`
- **Use**: Necessary for transmitting secure data via URLs.

---

### 🔤 ASCII (American Standard Code for Information Interchange)

Standard character encoding set that represents text on computers.

- **Example**: `72 101 108 108 111` (in decimal) → `“Hello”`
- **Use**: Basis for several modern encodings (UTF-8, etc.).

---

### 🔢 Binary Encoding

Represents characters using sequences of 0s and 1s (bits).

- **Example**: `“01001000 01100101 01101100 01101100 01101111”` → `“Hello”`
- **Use**: Low-level communication between systems.

---

### 📦 Base64

Encodes binary data as ASCII text using 64 characters (A-Z, a-z, 0-9, +, and /).

- **Example**: `“Hello”` → `“SGVsbG8=”`
- **Use**: Embedding binary data (such as images) in text, for example in emails or JSON.

---

### 📦 Base32

Similar to Base64, but uses 32 characters that are safe for filenames and URLs.

- **Example**: `“Hello”` → `“JBSWY3DP”`
- **Usage**: Safe alternative to Base64 when compatibility with special character-sensitive systems is required.

---

### 🧩 HTML Character Entities

Represents special characters in HTML with an entity starting with `&`.

- **Example**: `“&lt;”` → `“<”`
- **Usage**: Prevention of HTML/JS code injection (XSS).

---

### 📄 Quoted-Printable

Encoding used in emails to transmit binary data or special characters in ASCII text.

- **Example**: `“Hello=0AWorld”` → `“Hello\nWorld”`
- **Usage**: Used by MIME for sending emails with special characters.

---

### 📁 UUEncoding (Unix-to-Unix Encoding)

Encodes binary data into text for transmission between Unix systems.

- **Example**: `.uu` files containing encoded data.
- **Usage**: Communication between systems that do not directly support binary data.

  
---
## Conversion:

* **Hexadecimal**: Conversion of hexadecimal strings to text, using the built-in functions `bytes.fromhex` () and `.decode()` from Python
* **Binary**: Decoding of binary strings to ASCII characters, using the built-in functions `chr()` and `int()`.
* **Base64**: Use of the `base64` module for decoding `Base64`, using the `base64.b64decode()` and `.decode()` functions.
* **Base32**: Use of the `base64` module for decoding `Base32`, using the functions `base64.b64decode()` and `.decode()`.
* **Quoted-Printable**: Manipulation of bytes with the `quopri` and `io.BytesIO` modules, using the functions `io.BytesIO()`, `quopri.decode()`, `.decode()`, and `.getvalue()`
* **HTML Entities**: Conversion of HTML entities (`&lt;`, `&gt;`, etc.) to their corresponding characters, using the html module and the `html.unescape()` function    
* **UUencoding**: Decoding data in UUencode format using the `uu` module, using the functions `io.BytesIO()`, `.getvalue()`, `.decode()`, and `.encode()`

  
---


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

