import re
import os
from collections import Counter 
import pandas as pd

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

# CALCULATING TF AND IDF AND TF.IDF
# [word] = idf
word_idf = {}

# [(word, doc)] = tf
word_doc_tf = {}

# [(word, doc)] = tf.idf
tf_idf = {}


for file_name in os.listdir(data_dir):
    full_path = data_dir + '\\' + file_name
    num_of_documents += 1
    with open(full_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()
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

            word_doc_tf[(key, file_name)] = doc_counter[key] / doc_data["word_count"]


# Sort by alph. order
total_words_data = dict(sorted(total_words_data.items()))
print(f"Total words: {len(total_words_data)}")

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


# IDF Calculation, TF.IDF Calculation
for word in total_words_data.keys():
    word_idf[word] = num_of_documents / doc_freq_of_word(word)

    for doc in list_of_documents:
        try:
            tf_idf[(word, doc)] = word_doc_tf[(word, doc)] * word_idf[word]
        except KeyError as e:
            # every word has an IDF, but might not have a TF for a specific doc
            # if this error is thrown, (word, doc) pairing does not exist because
            # the doc never found the word in it
            # => TF = 0
            word_doc_tf[(word, doc)] = 0
            tf_idf[(word, doc)] = 0

word_idf = dict(sorted(word_idf.items()))

def all_data_for_word_in_doc(word: str, doc: str):
    return {
        "doc_word_freq": documents_data[doc]["word_frequency"][word],
        "doc_word_count": documents_data[doc]["word_count"],
        "doc_list": total_words_data[word]
    }



# Data Organization/Visualization:
all_data = []

for file_name in list_of_documents:
    for word in total_words_data.keys():
        all_data.append({
            "word": word,
            "in_doc": file_name,
            "TF": word_doc_tf[(word, file_name)],
            "IDF": word_idf[word],
            "TF.IDF": tf_idf[(word, file_name)]
        })

df = pd.DataFrame(all_data)

# chunk_size = 1000
# for i in range(0, len(df), chunk_size):
#     df.iloc[i:i+chunk_size].to_csv(f"all_data_part{i//chunk_size + 1}.csv", index=False)


# df.to_csv(f"all_data_whole.csv", index=False)