from flask import Flask, render_template, url_for,abort,request
app = Flask(__name__)
# import linebot related
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    LocationSendMessage, ImageSendMessage, StickerSendMessage,
    VideoSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction,
    PostbackEvent, ConfirmTemplate, CarouselTemplate, CarouselColumn,
    ImageCarouselTemplate, ImageCarouselColumn, FlexSendMessage
)
import json
app = Flask(__name__)
line_bot_api = LineBotApi('BGZBrkX6s+c8gpBVSwgrS5vKqED4bJvOpevQ404q+NuD3xHRIckH80WTGR+02oCyhnwS/S8F9PI7EanG4XXEBOn/SJqBL+fu+R1P6JDnURNYu3nu/KgFbNR8YP69Qo2weqHitqWpn/YcH5O/RZZFkgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c831cba596f59cc7379fc4133df6b6d8')
 
@handler.add(MessageEvent)
def handle_something(event):
    if event.message.type=='text':
        recrive_text=event.message.text
        if '輸入書名' in recrive_text:
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
            def get_books_list():
    #抓取網頁
                res = requests.get(get_url(bookName), headers=header)
                res.encoding = 'utf-8'     #轉換編碼至UTF-8
                rawdata = res.json()
    
        
    # data = json.loads(res)
                for i in range(0,25):
                    print("第 "+str(i)+" 本")
                    print("書名: "+str(rawdata["docs"][i]["pnx"]["display"]["title"][0]))
                    isbn = "isbn" in rawdata["docs"][i]["pnx"]["addata"]
                    if(isbn):
                        print("ISBN", end=' ')
                        for i in rawdata["docs"][i]["pnx"]["addata"]["isbn"]:
                            print(str(i),end=' ')
                        print("\n")
                    else:
                       print("找不到")
                    print("\n")
            
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
            bookName=input('想搜尋國立中央大學圖書:')

            result = get_books_list() 


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        print('receive msg')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'
    # handle msg
@handler.add(MessageEvent)
def handle_something(event):
    if event.message.type=='text':
        recrive_text=event.message.text
        if '打開相機掃QR code' in recrive_text:
            import cv2
            import pyzbar.pyzbar as pyzbar
            import numpy as np

            def barcode(gray):
    # test
                texts = pyzbar.decode(gray)
                if texts == []:
                    angle = barcode_angle(gray)
                    if angle < -45:
                        angle = -90 - angle
                    texts = bar(gray, angle)
                if texts == []:
                    gray = np.uint8(np.clip((1.1 * gray + 10), 0, 255))
                    angle = barcode_angle(gray)
                    if angle < -45:
                        angle = -90 - angle
                    texts = bar(gray, angle)
                return texts

            def bar(image, angle):
                gray = image
                bar = rotate_bound(gray, 0 - angle)
                roi = cv2.cvtColor(bar, cv2.COLOR_BGR2RGB)
                texts = pyzbar.decode(roi)
                return texts


            def barcode_angle(image):
                gray = image
                ret, binary = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
                kernel = np.ones((8, 8), np.uint8)
                dilation = cv2.dilate(binary, kernel, iterations=1)
                erosion = cv2.erode(dilation, kernel, iterations=1)
                erosion = cv2.erode(erosion, kernel, iterations=1)
                erosion = cv2.erode(erosion, kernel, iterations=1)
    
                contours, hierarchy = cv2.findContours(
                    erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                if len(contours) == 0:
                    rect = [0, 0, 0]
                else:
                    rect = cv2.minAreaRect(contours[0])
                return rect[2]

            def rotate_bound(image, angle):
                (h, w) = image.shape[:2]
                (cX, cY) = (w // 2, h // 2)

                M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
                cos = np.abs(M[0, 0])
                sin = np.abs(M[0, 1])
                nW = int((h * sin) + (w * cos))
                nH = int((h * cos) + (w * sin))

                M[0, 2] += (nW / 2) - cX
                M[1, 2] += (nH / 2) - cY

                return cv2.warpAffine(image, M, (nW, nH))

            image=cv2.imread(r"C:/Users/tc_li.LAPTOP-80MLFSGM/Desktop/AI/bar_1.jpg") #檔名無法使用中文
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            texts = barcode(gray)
            print(texts)
            if texts==[]:
                print("未識別成功")
            else:
                for text in texts:
                    tt = text.data.decode("utf-8")
                print("識別成功")
                print(tt)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user info & message
    user_id = event.source.user_id
    msg = event.message.text
    user_name = line_bot_api.get_profile(user_id).display_name
    
    # get msg details
    print('msg from [', user_name, '](', user_id, ') : ', msg)

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text = msg))

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
