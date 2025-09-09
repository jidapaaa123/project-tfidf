import re
import os
from collections import Counter 

root_dir = os.getcwd()
data_dir = root_dir + (r"\data")
delimiting_pattern = r'[ .,-]'

num_of_documents = 0
list_of_documents = []

# word: {word, # of documents with it}
# [word] = docs_list
total_words_data = {}

# document: {word freq. table, word count}
# [document] = {word_frequency, word_count}
documents_data = {}


for file_name in os.listdir(data_dir):
    full_path = data_dir + '\\' + file_name
    num_of_documents += 1
    with open(full_path, 'r', encoding='utf-8') as file:
        content = file.read()
        split_results = re.split(delimiting_pattern, content)
        words = [r for r in split_results if r.strip()]
        doc_counter = Counter(words)
        doc_data = {
            "word_frequency": doc_counter,
            "word_count": len(words)
        }
        documents_data[file_name] = doc_data
        list_of_documents.append(file_name)

        for key in doc_counter.keys():
            if key not in total_words_data:
                total_words_data[key] = [file_name]

            else:
                total_words_data[key].append(file_name)


def word_count_of_doc(file_name: str):
    full_path = data_dir + '\\' + file_name
    return documents_data[file_name]['word_count']

def word_freq_in_doc(word: str, file_name: str):
    full_path = data_dir + '\\' + file_name
    return documents_data[file_name]['word_frequency'][word]

def word_data_in_doc(file_name: str):
    full_path = data_dir + '\\' + file_name
    return documents_data[file_name]['word_frequency']

def doc_freq_of_word(word: str):
    return len(total_words_data[word])


print(word_count_of_doc("gatech.txt"))
print(list_of_documents)
print(list_of_documents.index("gatech.txt"))
print(doc_freq_of_word("mission"))