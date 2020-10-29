# import libraries
import requests
from bs4 import BeautifulSoup
import re

url = 'https://rsshub.app/lofter/tag/带卡/date'

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
titles = soup.find_all('title')
authuors = soup.find_all('author')
links = soup.find_all('guid')
titxts =[]
autxts =['/Author:']
ltxts = ['/Address:']

for i in range(0,len(titles)):
    titagtxt = (str(titles[i]))
    titxt = re.findall(r"<title><!\[CDATA\[(.+?)]]></title>",titagtxt)
    titxts.append(str(titxt))

for i in range(0,len(authuors)):
    autagtxt = (str(authuors[i]))
    autxt = re.findall(r"<author><!\[CDATA\[(.+?)]]></author>",autagtxt)
    autxts.append(str(autxt))

for i in range(0,len(links)):
    ltagtxt = (str(links[i]))
    ltxt = re.findall(r"<guid\ ispermalink=\"false\">(.+?)</guid>",ltagtxt)
    ltxts.append(str(ltxt))

article = ''

for i in range(0,len(titxts)):
    article = article + titxts[i]+'By'+ autxts[i] + '\nLink:'+ ltxts[i]+'\n\n'

with open('scraped_text.txt', 'w') as file:
    file.write(article)


