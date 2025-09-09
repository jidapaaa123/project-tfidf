import re
import os
from collections import Counter 
import pandas as pd

root_dir = os.getcwd()
data_dir = root_dir + (r"\data")
delimiting_pattern = r'[ .,-]'

num_of_documents = 0
documents_data = {}


for file_name in os.listdir(data_dir):
    # print(f"Reading {file_name}: ")
    full_path = data_dir + '\\' + file_name
    num_of_documents += 1
    with open(full_path, 'r', encoding='utf-8') as file:
        content = file.read()
        split_results = re.split(delimiting_pattern, content)
        words = [r for r in split_results if r.strip()]
        # print(Counter(words))
        doc_data = {
            "word_frequency": Counter(words),
            "word_count": len(words)
        }
        s = pd.Series(doc_data, name="word_count")
        df = s.to_frame()
        documents_data[file_name] = doc_data
        # print(df)
        
        # if ("gatech" in file_name):
        #     print(doc_data)
        # df = pd.DataFrame.from_dict(doc_data, orient="index")


def word_count_of_doc(file_name: str):
    full_path = data_dir + '\\' + file_name
    return documents_data[file_name]['word_count']

def word_freq_in_doc(word: str, file_name: str):
    full_path = data_dir + '\\' + file_name
    return documents_data[file_name]['word_frequency'][word]


print(word_count_of_doc("gatech.txt"))
print(word_freq_in_doc("mission", "gatech.txt"))
