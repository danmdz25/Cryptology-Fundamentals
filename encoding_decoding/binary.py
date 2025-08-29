with open ("encoding_decoding/binary.txt","r") as f:
    binary = f.read()

binary_w_comma = binary.replace(" ",",")
binary_list = binary_w_comma.split(",")
phrase = ""
for i in binary_list:
    decode_text = chr(int(i,2))
    phrase += decode_text

print(phrase)
