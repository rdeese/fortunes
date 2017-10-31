from lxml import html
import requests
from unidecode import unidecode

FORTUNE_PAGE = 'https://www.goodreads.com/quotes/tag/inspirational?page={}'

corpus = open('inputs/goodreads-inspiration.txt', 'w')

for page in range(0, 101):
    print("Scraping page {}...".format(page))
    page = requests.get(FORTUNE_PAGE.format(page))
    tree = html.fromstring(page.content)
    content = tree.xpath('//div[@class="quoteText"]/text()')
    content = '\n'.join(content)
    corpus.write(content)

corpus.close()
