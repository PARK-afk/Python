from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
soup = bs(html.text, 'html.parser')

data1 = soup.find('div',{'class':'detail_box'})
pprint(data1)

data2 = data1.find_all('dd')
pprint(data2)
data3 = [x.get_text() for x in data2]
pprint(data3)