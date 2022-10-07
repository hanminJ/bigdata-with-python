"""import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
webpage=requests.get("https://www.daangn.com/hot_articles")
soup=BeautifulSoup(webpage.content,'html.parser')
#result = soup.find_all('h2',class_='card-title')

#for data in result:
#    print(data.text)
#for child in soup.ul.children - 하면  ul태그 아래 후손들만 뺴옴

# ol ul 포함 리소스를 찾고 싶다면

#import re
#print(soup.find_all(re.compile('[ou]l'))) re패턴이용해서 간편하게
#print(soup.find_all(re.compile('h[1-3]')))
#print(soup.find_all(['h1','p'])) 리스트
#print(soup.select('.card-region-name'))  클래스 이용

#아이디 이용 크롤링
#download = soup.select('#hot-articles-go-download')
#print(download)

title = soup.select('.card-title')
for t in title:
    print(t.get_text())
"""

""" 
태그 선택가 
아이디 선택자 #
클래스 선택자 .
웹 크롤링
requests 라이브러리 : 특정사이트의 hrml 통쨰로 긇어옴
beautifulsoup 라이브러리 : 내부로 객체화를 함
태그 기반 find all
css 기반 select

"""
'''
import pandas as pd
import openpyxl as xl
import requests
from bs4 import BeautifulSoup as bs

webpage=requests.get("https://library.gabia.com/")
soup=bs(webpage.text,'html.parser')
result =soup.select('div.esg-entry-content a.eg-grant-element-0')

titles=[]
links=[]

for index,element in enumerate(result,1):
    titles.append(element.text)
    links.append(element.attrs['href'])

df=pd.DataFrame()
df['titles']=titles
df['links']=links

df.to_excel('./data.xlsx',sheet_name = 'sheet1')

#print("{}번쨰 게시글 : {},{}".format(index,element.text,element.attrs['href']))

#for t in result:
# print(t.get_text())
'''

