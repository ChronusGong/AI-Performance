import re
from bs4 import BeautifulSoup
from collections import Counter, defaultdict

WORD_TO_SPLIT_ON = 'PART I'


def process_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    clean_text = soup.get_text()
    parts = clean_text.split(WORD_TO_SPLIT_ON)
    if len(parts) > 1:
        temp = WORD_TO_SPLIT_ON.join(parts[1:])
    else:
        temp = clean_text

    temp = re.sub(r'[^\w\s]', '', temp)
    temp = re.sub(r'\d+', '', temp)
    result = temp.lower()
    return result


if __name__ == '__main__':
    with open('annual-report/pfizer-2023-10k.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('keywords.txt', 'r', encoding='utf-8') as file:
        keyword_file = file.read()

    keyword_file = keyword_file.lower()

    keywords = keyword_file.split(',')

    text = process_html(html)

    words_and_phrases = re.findall(r'\b\w+\b', text)

    keyword_counts = defaultdict(int)

    for keyword in keywords:
        keyword_counts[keyword] = 0

    for word in words_and_phrases:
        if word in keyword_counts:
            keyword_counts[word] += 1

    total_keyword_frequency = sum(keyword_counts.values())

    print(f"The total keyword frequency is: {total_keyword_frequency}")
