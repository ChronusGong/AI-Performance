import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

folder_path = 'data'
contents = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            contents.append(file.read())

# initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))


# transfer document to TF-IDF feature matrix
tfidf_matrix = vectorizer.fit_transform(contents)

feature_names = np.array(vectorizer.get_feature_names_out())

# print tf-idf scores
tfidf_scores = tfidf_matrix.toarray().flatten()
for word, score in zip(feature_names, tfidf_scores):
    if score > 0:
        print(f'{word}: {score}')