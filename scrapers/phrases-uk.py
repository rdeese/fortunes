from lxml import html
import requests
from unidecode import unidecode

PAGE = 'https://www.phrases.org.uk/meanings/proverbs.html'

corpus = open('inputs/phrases-uk.txt', 'w')

page = requests.get(PAGE)
tree = html.fromstring(page.content)
plain_content = tree.xpath('//p[@class="phrase-list"]/text()')
links_content = tree.xpath('//p[@class="phrase-list"]/a/text()')
content = '\n'.join(plain_content) + '\n' + '\n'.join(links_content)
corpus.write(content)

corpus.close()
