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

# 中央大學圖書館api
url='https://ncu.primo.exlibrisgroup.com/primaws/rest/pub/pnxs'

# api 網址
# https://ncu.primo.exlibrisgroup.com/primaws/rest/pub/pnxs?blendFacetsSeparately=false&disableCache=false&getMore=0&inst=886UST_NCU&lang=en&limit=25&newspapersActive=false&newspapersSearch=false&offset=0&pcAvailability=false&q=any,contains,python&qExclude=&qInclude=&rapido=false&refEntryActive=false&rtaLinks=true&scope=usttest&skipDelivery=Y&sort=rank&tab=Everything&vid=886UST_NCU:886UST_NCU

# 抓取網頁的主程式
def get_books_list(bookName):
    #抓取網頁
    res = requests.get(get_url(bookName), headers=header)
    res.encoding = 'utf-8'     #轉換編碼至UTF-8
    rawdata = res.json()
    book_data =[]
    ISBN = []
    # data = json.loads(res)
    for i in range(0,25):
        print("第 "+str(i)+" 本")
        print("書名: "+str(rawdata["docs"][i]["pnx"]["display"]["title"][0]))
        isbn = "isbn" in rawdata["docs"][i]["pnx"]["addata"]
       
        if(isbn):
            print("ISBN", end=' ')
            for j in rawdata["docs"][i]["pnx"]["addata"]["isbn"]:
                ISBN.append(str(j))
                print("ISBN"+str(j),end=' ')
            tmp ={
                '次數':i, 
                '書名': rawdata["docs"][i]["pnx"]["display"]["title"][0],
                'ISBN':ISBN
            }
                
            
            print("\n")
        else:
            tmp ={
                '次數':i, 
                '書名': rawdata["docs"][i]["pnx"]["display"]["title"][0],
                'ISBN': 0
            }
            print("找不到")
            print("\n")
        
        book_data.append(tmp.copy())
        ISBN.clear()
        tmp.clear()
    return book_data
               
# 抓取網頁連結
def get_url(bookName):    
    blendFacetsSeparately='false'
    disableCache='false'
    getMore='0'
    inst='886UST_NCU'
    lang='en'
    limit='25'
    newspapersActive='false'
    newspapersSearch='false'
    offset='0'
    pcAvailability='false'
    input={bookName}
    qExclude=''
    qInclude=''
    rapido='false'
    refEntryActive='false'
    rtaLinks='true'
    scope='usttest&skipDelivery=Y'
    sort='rank'
    tab='Everything'
    vid='886UST_NCU:886UST_NCU'
    
    query = f"?blendFacetsSeparately={blendFacetsSeparately}&disableCache={disableCache}&getMore={getMore}&inst={inst}&lang={lang}&limit={limit}&newspapersActive={newspapersActive}&newspapersSearch={newspapersSearch}&offset={offset}&pcAvailability={pcAvailability}&q=any,contains,{input}&qExclude={qExclude}&qInclude={qInclude}&rapido={rapido}&refEntryActive={refEntryActive}&rtaLinks={rtaLinks}&scope={scope}&sort={sort}&tab={tab}&vid={vid}"
    
    news_list_url = url + '?' + query
            
    return news_list_url

# 使用者輸入參數
def receive_bookdata(bookName):
    result = get_books_list(bookName)
    
    # print("result:\n")
    # print(result)
    str_message=''
    i=0
    for book in result:
        i+=1
        str_message += f"第{i}本: {book['書名']} {book['ISBN']}\n"
    return str_message