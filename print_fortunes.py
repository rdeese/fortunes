""" Script to write a page of fortunes as a PDF """

import os
import random
import re
import pickle
import markovify

FORTUNE_TEMPLATE = "\\fortune{FORTUNE}{NUMBERS}"
PICKLED_MODEL = 'fortune_model.pickle'

FIRST_PERSON_PRONOUN = re.compile(r'(\W|\A)I(\W|\Z)|(\W|\A)me(\W|\Z)', flags=re.IGNORECASE)

def lucky_numbers():
    """ Return a string of 6 ordered, comma-separated numbers """
    sorted_numbers = sorted([random.randint(1, 100) for _ in range(6)])
    return ', '.join([str(x) for x in sorted_numbers])

def valid_fortune(fortune):
    """ Whether this fortune is valid """
    return (fortune is not None and
            FIRST_PERSON_PRONOUN.search(fortune) is None)

def main():
    """ Generate fortunes in a PDF """
    with open('inputs/clean_corpus.txt') as corpus_file:
        corpus = corpus_file.read()

    if not os.path.isfile(PICKLED_MODEL):
        model = markovify.Text(corpus, state_size=3)
        with open(PICKLED_MODEL, 'wb') as model_file:
            pickle.dump(model, model_file)
    else:
        with open(PICKLED_MODEL, 'rb') as model_file:
            model = pickle.load(model_file)

    fortunes = []
    null_fortunes_count = 0
    while len(fortunes) < 40:
        fortune = model.make_short_sentence(60)
        if valid_fortune(fortune):
            fortunes.append(fortune)
        else:
            null_fortunes_count += 1

    print("Generated {} fortunes with {} retries".format(40, null_fortunes_count))

    fortunes = [FORTUNE_TEMPLATE.replace("FORTUNE", fortune) for fortune in fortunes]
    fortunes = [fortune.replace("NUMBERS", lucky_numbers()) for fortune in fortunes]
    fortunes_block = '\n'.join(fortunes)

    with open('tex/fortunes-template.tex') as template_file:
        template = template_file.read()

    with open('tex/fortunes.tex', 'w') as fortunes_file:
        fortunes_file.write(template.replace("FORTUNE-CONTENT", fortunes_block))

    os.system('cd tex && xelatex fortunes.tex')

if __name__ == '__main__':
    main()
