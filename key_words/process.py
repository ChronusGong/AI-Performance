import re

with open('./data/Deloitte-2022-1.txt', 'r', encoding='utf-8') as file:
    content = file.read()

cleaned_text = re.sub(r'[^j\w^s]', ' ', content) # keep letters, numbers and space
cleaned_text = cleaned_text.lower() # lower all the letters

with open('./data/Deloitte-2022-1.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)