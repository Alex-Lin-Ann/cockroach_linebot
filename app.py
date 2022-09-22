from linebot import LineBotApi
from linebot.models import TextSendMessage
import time

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('zYXfWsIEAgAiqGoU62iLIdiPDsIVsz5t1W0lr3urkwyemRmrfTZBCKauljVvoYqKFX71W08VEzNuIceqtoqWRBIiAefZAo8fKXJV9HgpxuCv+DXUIbVc5v8RwsMbRqb9J014bZrgo+e3TYZoPD3Y4AdB04t89/1O/w1cDnyilFU=')
# 請填入您的ID
yourID = 'U61a52960fc6fb48ae57da4f63bf06497'
# 主動推播訊息
line_bot_api.push_message(yourID, 
                          TextSendMessage(text='安安您好！早餐吃了嗎？'))
# 用迴圈推播訊息
for i in [1,2,3,4,5]:
    line_bot_api.push_message(yourID, 
                              TextSendMessage(text='我們來倒數：'+str(i)))
    time.sleep(1)