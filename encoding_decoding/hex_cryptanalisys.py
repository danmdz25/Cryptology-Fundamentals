with open('hex_encoding.txt','r') as f:
    hex_string = f.read()

bytes_object = bytes.fromhex(hex_string).decode('utf-8')
print(bytes_object)