from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)
soup = bs(html.text, 'html.parser')
# pprint(soup)

data1 = soup.select_one('div.today_area > div.main_info > div.info_data > span.todaytemp')
pprint(data1)