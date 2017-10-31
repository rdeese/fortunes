from lxml import html
import requests
from unidecode import unidecode

FORTUNE_PAGE = 'http://www.fortunecookiemessage.com/archive.php?start={}'

corpus = open('inputs/fortunecookiemessage.txt', 'w')

for start_index in range(0, 850, 50):
    print("Scraping fortunes {} through {}...".format(start_index, start_index + 49))
    page = requests.get(FORTUNE_PAGE.format(start_index))
    tree = html.fromstring(page.content)
    content = tree.xpath('//table[@class="table1"]/tr/td/a/text()')
    content = '\n'.join(content)
    corpus.write(content)

corpus.close()
