# import flask related
from flask import Flask, request, abort, url_for
from urllib.parse import parse_qsl, parse_qs

from linebot.models import events
from line_chatbot_api import *

import random

from service_actions.main_func import *
# create flask server
app = Flask(__name__)

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
def handle_message(event):
    if event.message.type == 'text':
        recrive_text = event.message.text
        
        print('receive text', recrive_text)
        if '查詢' in recrive_text:
            # 所有事情在service_actions做
           call_main(event)    

@handler.add(PostbackEvent)
def handle_postback(event):
    user_id = event.source.user_id
    user_name = line_bot_api.get_profile(user_id).display_name
    # print(event.postback.data)
    postback_data = dict(parse_qsl(event.postback.data))
    # print(postback_data.get('action', ''))
    # print(postback_data.get('item', ''))
    
    if postback_data.get('action')=='輸入文字':
        messages=[]
        print('輸入文字')
        messages.append(TextSendMessage(text='請輸入要搜尋書名'))
        line_bot_api.reply_message(event.reply_token, messages)
        
    elif postback_data.get('action')=='掃QRcode':
        messages=[]
        print('掃QRcode')
        messages.append(TextSendMessage(text='掃QRcode'))
        line_bot_api.reply_message(event.reply_token, messages)
    

    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566, debug=True)
