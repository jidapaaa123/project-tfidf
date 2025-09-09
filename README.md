To keep things simple:

Each "word" is defined by separation of white space or any of the following punctuations: . , -.
(I chose these by literally CTRL-F'ing the mission statements for all punctuations on the regular keyboard. You can see 'aggregate.txt' of the remnants of that process)

Thus, "Tech" and "Tech's" will be recognized as different words

Words are transformed to all-lowercase to proof out case-sensitivity

BRAINSTORMING NOTES:
# [document d] = {word_frequency, word_count}
TF(t, d) -> found in documents_data (word freq of t in doc d, word count in doc d)

# [word t] = docs_list
IDF(t) -> found in total_words_data (length of docs_list for word t)