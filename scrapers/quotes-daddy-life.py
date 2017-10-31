from lxml import html
import requests
from unidecode import unidecode

FORTUNE_PAGE = 'https://www.quotesdaddy.com/tag/Life/{}'

corpus = open('inputs/quotes-daddy-life.txt', 'w')

for page in range(0, 2001):
    print("Scraping page {}...".format(page))
    page = requests.get(FORTUNE_PAGE.format(page))
    tree = html.fromstring(page.content)
    content = tree.xpath('//div[@class="quoteText"]/p/a/text()')
    content = '\n'.join(content)
    corpus.write(content)
    corpus.write('\n')

corpus.close()
