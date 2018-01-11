from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage

class bot:
    an = 'U3c6a47257d656187515d46072a337333'

    root_id = 'U99bd52a54e27fedddf25c0ac9440b88a'

    token = 'cDg0cSra/yUdJSUTkfvu6tdvTneYPpMsoFh12H+pRoHKGU5LO6yFm8VmWJCCLaExLbM6o3ZDHPQQ3Dlesd3aZf1kBKL8scGl+4O4Hp/jdZygUBDHr5P6mtbBDKRASpp7pigZp6yUZ8Ur+jPEtsVBLwdB04t89/1O/w1cDnyilFU='
    secre = 'b352eb7c0aed94d0009326e7ae46cd70'

    def send_text(self, msg):
        line_bot_api = LineBotApi(self.token)
        line_bot_api.push_message(an, TextSendMessage(text=msg))
