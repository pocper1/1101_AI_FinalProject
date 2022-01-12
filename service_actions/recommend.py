# 載入所需的工具
import requests
from bs4 import BeautifulSoup
#import time
#import pandas as pd


bookName = input("請輸入要查詢的書籍：")

# 取得查詢書籍頁面
resp = requests.get("https://search.books.com.tw/search/query/key/" + bookName +"/cat/all")
soup = BeautifulSoup(resp.text, 'html.parser')

# 取得書籍位置
info_items = soup.find_all('a', target="_blank", rel="mid_name")
for item in info_items:
    name = item.get('title')
    print(name)
  
info_items = soup.find_all('a', rel="go_author")
for item in info_items:
    author = item.get('title')
    print(author)
  
