from __future__ import unicode_literals
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage
import requests
import json
import configparser
import os
from urllib import parse
app = Flask(__name__, static_url_path='/static')
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])


config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))
my_line_id = config.get('line-bot', 'my_line_id')
end_point = config.get('line-bot', 'end_point')
line_login_id = config.get('line-bot', 'line_login_id')
line_login_secret = config.get('line-bot', 'line_login_secret')
my_phone = config.get('line-bot', 'my_phone')
HEADER = {
    'Content-type': 'application/json',
    'Authorization': F'Bearer {config.get("line-bot", "channel_access_token")}'
}


# @app.route("/", methods=['POST', 'GET'])
# def index():
#     if request.method == 'GET':
#         print('OK')
#         return 'ok'
#     body = request.json
#     events = body["events"]
#     print(body)
#     if "replyToken" in events[0]:
#         payload = dict()
#         replyToken = events[0]["replyToken"]
#         payload["replyToken"] = replyToken
#         if events[0]["type"] == "message":
#             if events[0]["message"]["type"] == "text":
#                 text = events[0]["message"]["text"]

#                 if text == "start":
#                     payload["messages"] = [getCockEmojiMessage(),
#                                     getNameEmojiMessage(),
#                                     getCockroachImageMessage()
#                                     ]
#                 else:
#                     payload["messages"] = [
#                             {
#                                 "type": "text",
#                                 "text": text
#                             }
#                         ]
#                 replyMessage(payload)
#             else:
#                 data = json.loads(events[0]["postback"]["data"])
#                 action = data["action"]
#                 if action == "get_near":
#                     data["action"] = "get_detail"
#                 elif action == "get_detail":
#                     del data["action"]
#                     payload["messages"] = [getCockroachImageMessage()]
#                 replyMessage(payload)

#     return 'OK'


def pushmsg(request):
#   try:
    msg = request.args.get('msg')
    # if msg == '1':
    line_bot_api.push_message(my_line_id, TextSendMessage(text='hello'))
    # elif msg == '2':
    line_bot_api.push_message(my_line_id, StickerSendMessage(package_id=1, sticker_id=2))
    # elif msg == '3':
    imgurl = 'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png'
    line_bot_api.push_message(my_line_id, ImageSendMessage(original_content_url=imgurl, preview_image_url=imgurl))
    # elif msg == '4':
    line_bot_api.push_message(my_line_id, LocationSendMessage(title='總統府',
                                                address='100台北市中正區重慶南路一段122號',
                                                latitude='25.040319874750914',
                                                longitude='121.51162883484746'))
    # else:
    msg = 'ok'
    return msg
#   except:
    # print('error')


@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
        )


@app.route("/sendTextMessageToMe", methods=['POST'])
def sendTextMessageToMe():
    pushMessage({})
    return 'OK'

def getNameEmojiMessage():
    lookUpStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    productId = "5ac21a8c040ab15980c9b43f"
    name = "Cockroach"
    message = dict()
    message["type"] = "text"
    message["text"] = "".join("$" for r in range(len(name)))
    emojis_list = list()
    for i, nChar in enumerate(name):
        emojis_list.append(
            {
              "index": i,
              "productId": productId,
              "emojiId": f"{lookUpStr.index(nChar) + 1 :03}"
            }
        )
    message["emojis"] = emojis_list
    return message

def getCockEmojiMessage():
    lookUpStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    productId = "5ac21a8c040ab15980c9b43f"
    name = "FindOut"
    message = dict()
    message["type"] = "text"
    message["text"] = "".join("$" for r in range(len(name)))
    emojis_list = list()
    for i, nChar in enumerate(name):
        emojis_list.append(
            {
              "index": i,
              "productId": productId,
              "emojiId": f"{lookUpStr.index(nChar) + 1 :03}"
            }
        )
    message["emojis"] = emojis_list
    return message

def getCockroachImageMessage(originalContentUrl=F"{end_point}/static/cockroach.jpeg"):
    return getImageMessage(originalContentUrl)


def getImageMessage(originalContentUrl):
    message = {
      "type": "image",
      "originalContentUrl": originalContentUrl,
      "previewImageUrl": originalContentUrl
    }

    return message


def replyMessage(payload):
    r = requests.post('https://api.line.me/v2/bot/message/reply', data=json.dumps(payload), headers=HEADER)
    print(r.content)
    return 'OK'


def pushMessage(payload):
    r = requests.post('https://api.line.me/v2/bot/message/push', data=json.dumps(payload), headers=HEADER)
    print(r.content)
    return 'OK'


def getTotalSentMessageCount():
    r = requests.get('https://api.line.me/v2/bot/message/quota/consumption', headers=HEADER)
    print(r.json())
    return r.json()['totalUsage']

if __name__ == "__main__":
    app.debug = True
    app.run()
