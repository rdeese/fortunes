from lxml import html
import requests
from unidecode import unidecode

PAGE = 'http://www.myafricanow.com/best-african-proverbs/'

corpus = open('inputs/myafricanow-proverbs.txt', 'w')

page = requests.get(PAGE)
tree = html.fromstring(page.content)
plain_content = tree.xpath('//li/text()')
links_content = tree.xpath('//li/strong/text()')
content = '\n'.join(plain_content) + '\n' + '\n'.join(links_content)
corpus.write(content)

corpus.close()
