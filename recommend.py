import requests
import datetime
import json

# 引入 Beautiful Soup 模組
from bs4 import BeautifulSoup

# import time
# import random
# import threading
# import pprint
# import concurrent.futures
# from time import sleep
# from tqdm import tqdm, trange
# import pandas as pd


header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36'}

# 柏克萊中文書api
url='http://www.w3.org/TR/html4/strict.dtd'
# api 網址
# https://www.books.com.tw/web/books

def get_books_list():
    res = requests.get(get_url(bookName), headers=header)
    res.encoding = 'utf-8'     #轉換編碼至UTF-8
    rawdata = res.json()
    
        
    # data = json.loads(res)
    for i in range(0,25):
        print("推薦書籍:")
        print("第 "+str(i)+" 本")
        print("書名: "+str(rawdata["docs"][i]["pnx"]["display"]["title"][0]))
        isbn = "isbn" in rawdata["docs"][i]["pnx"]["addata"]
        
            

# 使用者輸入參數
bookName=input('isbn:')

result = get_books_list()
