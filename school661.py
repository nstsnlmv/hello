import requests
from bs4 import BeautifulSoup

result = {}
r = requests.get("http://www.school661.spb.ru/")
r.encoding = 'windows-1251'

soup = BeautifulSoup(r.text, 'lxml')

subjects = soup.findAll('td', {'width': '312'})
dates = soup.findAll('td', {'width': '350'})

for s, d in zip(subjects, dates):
    result.update({s.text: d.text})

print(result['обществознание'])


