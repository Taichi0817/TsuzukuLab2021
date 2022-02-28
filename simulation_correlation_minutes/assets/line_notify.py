import requests
import os


from . import secret

def main(message='演算終了'):
    line_notify_token = 'akHLNAuC8XmSHLXRuOMChlMe3FpfmU2E8KoWXzf21wL'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

def main_gazo(name_of_image, message):
    url = "https://notify-api.line.me/api/notify"
    token = secret.secret
    headers = {"Authorization" : "Bearer "+ token}

    payload = {"message" :  message}
    #imagesフォルダの中のgazo.jpg
    files = {"imageFile":open('./images/{}'.format(name_of_image),'rb')}
    # rbはバイナリファイルを読み込む
    post = requests.post(url ,headers = headers ,params=payload,files=files)