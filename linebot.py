from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage

class bot:
    root_id = ['U99bd52a54e27fedddf25c0ac9440b88a']

    usr_id  = [ 'U1c5963fc1852528a71dd6aec6d155c7b','U7b669e94630f883c6c2899dca3ed9fea',
			    'Uaaa5c3567e84e275fe939cef6859b0b5','U8da72ed69be8a2ed8dd7fc336505ffa1',
			    'U99bd52a54e27fedddf25c0ac9440b88a','U94390a4394bdc2fb4d56516fc1ba1630',
			    'Uf376616c70c838e8b10c29531decee3a','Ud8cb235b5f85f8a71a4a01e20b3eb45a']
    '''
    usr_name  = [ 
                '易新':'U1c5963fc1852528a71dd6aec6d155c7b',
                '竹源':'U7b669e94630f883c6c2899dca3ed9fea',
			    '碩錫':'Uaaa5c3567e84e275fe939cef6859b0b5',
                '小柯':'U8da72ed69be8a2ed8dd7fc336505ffa1',
			    '佳慶':'U99bd52a54e27fedddf25c0ac9440b88a',
                '阿哲':'U94390a4394bdc2fb4d56516fc1ba1630',
			    '俊傑':'Uf376616c70c838e8b10c29531decee3a',
                '博撤':'Ud8cb235b5f85f8a71a4a01e20b3eb45a'
                ]
    '''

    token = 'cDg0cSra/yUdJSUTkfvu6tdvTneYPpMsoFh12H+pRoHKGU5LO6yFm8VmWJCCLaExLbM6o3ZDHPQQ3Dlesd3aZf1kBKL8scGl+4O4Hp/jdZygUBDHr5P6mtbBDKRASpp7pigZp6yUZ8Ur+jPEtsVBLwdB04t89/1O/w1cDnyilFU='
    secre = 'b352eb7c0aed94d0009326e7ae46cd70'

    
    # 群發文字訊息
    def  multi_text(self, id, msg):
        LineBotApi(self.token).multicast(id, TextSendMessage(text=msg))

    # 群發圖片訊息
    def multi_img(self, id, img):
        image_message = ImageSendMessage(original_content_url = img, preview_image_url = img)                                    
        LineBotApi(self.token).multicast(id, image_message)
     




