""" Script to write a page of fortunes as a PDF """

import os
import pickle
import markovify

FORTUNE_TEMPLATE = "\\fortune{FORTUNE}"
PICKLED_MODEL = 'fortune_model.pickle'

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
        if fortune is not None:
            fortunes.append(fortune)
        else:
            null_fortunes_count += 1

    print("Generated {} fortunes with {} retries".format(40, null_fortunes_count))
    fortunes_block = '\n'.join([FORTUNE_TEMPLATE.replace("FORTUNE", fortune)
                                for fortune in fortunes])

    with open('tex/fortunes-template.tex') as template_file:
        template = template_file.read()

    with open('tex/fortunes.tex', 'w') as fortunes_file:
        fortunes_file.write(template.replace("FORTUNE-CONTENT", fortunes_block))

    os.system('cd tex && xelatex fortunes.tex')

if __name__ == '__main__':
    main()
