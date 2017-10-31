import markovify
import os

FORTUNE_TEMPLATE = "\\fortune{{}}\n"

with open('inputs/clean_corpus.py') as f:
    corpus = f.read()

model = markovify.Text(corpus, state_size=3)
fortunes = [FORTUNE_TEMPLATE.format(model.make_short_sentence(60)) for _ in range(40)]

with open('tex/fortunes.tex') as f:
    template = f.read()

with open('tex/fortunes.tex', 'w') as f:
    f.write(template.replace("FORTUNE-CONTENT", fortunes))

os.system('cd tex && xelatex fortunes.tex')
