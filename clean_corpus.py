from unidecode import unidecode

with open('inputs/corpus.txt', encoding='latin-1') as raw_corpus:
    clean_corpus = unidecode(raw_corpus.read())

with open('inputs/clean_corpus.txt', 'w') as f:
    f.write(clean_corpus)

