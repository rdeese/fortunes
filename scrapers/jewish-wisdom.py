from lxml import html
import requests
from unidecode import unidecode

FORTUNE_PAGE = 'http://www.jewish-wisdom.com/index.php?h=a&a=&p=&t=Any&l={}&submit=more'

corpus = open('inputs/jewish-wisdom.txt', 'w')

for start_index in range(0, 3100, 25):
    print("Scraping fortunes {} through {}...".format(start_index+1, start_index + 25))
    page = requests.get(FORTUNE_PAGE.format(start_index))
    tree = html.fromstring(page.content)
    content = tree.xpath('//div[@style="padding-right:120px;"]/text()')
    content = '\n'.join(content)
    corpus.write(content)

corpus.close()
