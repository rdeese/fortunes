from lxml import html
import requests
from unidecode import unidecode

FORTUNE_PAGE = 'https://www.successories.com/iquote/author/25510/english-16th-century-proverbs-quotes/{}'

corpus = open('inputs/successories-sixteenth-century.txt', 'w')

for page_number in range(1, 13):
    print("Scraping quotes page {}".format(page_number))
    page = requests.get(FORTUNE_PAGE.format(page_number))
    tree = html.fromstring(page.content)
    content = tree.xpath('//div[@class="quotebox"]/div[@class="quote"]/a/text()')
    content = '\n'.join(content)
    corpus.write(content)

corpus.close()
