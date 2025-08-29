import quopri
import io

with open('quoted-printable.txt', 'r') as f:
    encoded_data = f.read()

input_file = io.BytesIO(encoded_data.encode('utf-8'))
output_file = io.BytesIO()
quopri.decode(input_file, output_file)
decoded_bytes = output_file.getvalue()
decoded_string = decoded_bytes.decode('utf-8', errors='ignore')

print(decoded_string)

