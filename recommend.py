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


# 使用者輸入參數
bookName=input('推薦書籍:')

result = get_books_list()