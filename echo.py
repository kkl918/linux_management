from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

token = 'cDg0cSra/yUdJSUTkfvu6tdvTneYPpMsoFh12H+pRoHKGU5LO6yFm8VmWJCCLaExLbM6o3ZDHPQQ3Dlesd3aZf1kBKL8scGl+4O4Hp/jdZygUBDHr5P6mtbBDKRASpp7pigZp6yUZ8Ur+jPEtsVBLwdB04t89/1O/w1cDnyilFU='
secre = 'b352eb7c0aed94d0009326e7ae46cd70'

line_bot_api = LineBotApi('cDg0cSra/yUdJSUTkfvu6tdvTneYPpMsoFh12H+pRoHKGU5LO6yFm8VmWJCCLaExLbM6o3ZDHPQQ3Dlesd3aZf1kBKL8scGl+4O4Hp/jdZygUBDHr5P6mtbBDKRASpp7pigZp6yUZ8Ur+jPEtsVBLwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b352eb7c0aed94d0009326e7ae46cd70')



@app.route('/')
def index():
    return "<p>Hello World_2!</p>"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return ' '


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
