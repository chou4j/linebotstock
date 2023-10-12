from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['ajmR+KbLXRdm5q+U9UujjsVN5UwzQplff66FhzfI8NWbY03J8hICN2m0/knspH0pB7h2pf63BlsiXnynQgFn5sRzgg2RFr3E65jArO0XovFXG+ART+tTQMwrASEO9HpjszTHJprMEomhV9AvoFWctAdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['c2b360536f212750f872a894b186c43b'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)