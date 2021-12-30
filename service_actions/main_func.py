from linebot.models import messages
from line_chatbot_api import *
from service_actions.code_reader import *
from service_actions.get_library import *
from service_actions.recommend import *


def call_main(event):
    message = TemplateSendMessage(
        alt_text='選取查詢書籍方式',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/rfgMcFM.jpg',
            title='請問用什麼方式查詢書籍呢?',
            text='請在下方點選您想選取的方式',
            actions=[
                MessageAction(
                    label='輸入文字', 
                    text='輸入文字'
                ),
                MessageAction(
                    label='掃QRcode', 
                    text='掃QRcode'
                )
            ]
        )
    )
    send_text = event.message.text
    print('輸出文字:'+send_text)
    line_bot_api.reply_message(event.reply_token, message)
    
    
def call_input_text(event):
    messages = []
    messages.append(TextSendMessage(text='請輸入書名'))
    line_bot_api.reply_message(event.reply_token, messages) 
     
def call_qrcode(event):
    messages = []
    messages.append(TextSendMessage(text='請傳送一張QRcode 的照片'))
    line_bot_api.reply_message(event.reply_token, messages)  