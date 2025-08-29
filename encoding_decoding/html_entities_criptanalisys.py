import html 

with open('html_entities.txt', 'r') as file:
    encoded_data = file.read()
    decoded = html.unescape(encoded_data)

print(decoded)
