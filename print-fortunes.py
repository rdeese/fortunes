import markovify
import os

FORTUNE_TEMPLATE = "\\fortune{FORTUNE}"

with open('inputs/quotes-daddy-life.txt') as f:
    corpus = f.read()

model = markovify.Text(corpus, state_size=3)
fortunes = '\n'.join([FORTUNE_TEMPLATE.replace("FORTUNE", model.make_short_sentence(60)) for _ in range(40)])
print(fortunes)

with open('tex/fortunes-template.tex') as f:
    template = f.read()

with open('tex/fortunes.tex', 'w') as f:
    f.write(template.replace("FORTUNE-CONTENT", fortunes))

os.system('cd tex && xelatex fortunes.tex')
