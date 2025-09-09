import re
import os

root_dir = os.getcwd()
data_dir = root_dir + (r"\data")
print(data_dir)

delimiting_pattern = r'[ .,-]'
for file_name in os.listdir(data_dir):
    # print(f"Reading {file_name}: ")
    full_path = data_dir + '\\' + file_name
    with open(full_path, 'r', encoding='utf-8') as file:
        content = file.read()
        split_results = re.split(delimiting_pattern, content)
        words = [r for r in split_results if r.strip()]
        print(words)