import uu
import io

with open ('encoding_decoding/UUencoding.txt','r') as f:
    file= f.read().encode('utf-8')

input_file = io.BytesIO(file)
output_file = io.BytesIO()

uu.decode(input_file,output_file)

decoded_bytes = output_file.getvalue()
decoded_string = decoded_bytes.decode('utf-8', errors='ignore')
print(decoded_string)

