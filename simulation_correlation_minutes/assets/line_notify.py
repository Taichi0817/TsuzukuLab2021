import requests
import os

def main(message='演算終了'):
    line_notify_token = 'akHLNAuC8XmSHLXRuOMChlMe3FpfmU2E8KoWXzf21wL'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

def main_gazo(name_of_image):
    url = "https://notify-api.line.me/api/notify"
    token = "akHLNAuC8XmSHLXRuOMChlMe3FpfmU2E8KoWXzf21wL"
    headers = {"Authorization" : "Bearer "+ token}

    message = '演算終了'
    payload = {"message" :  message}
    #imagesフォルダの中のgazo.jpg
    files = {"imageFile":open('./images/{}'.format(name_of_image),'rb')}
    # rbはバイナリファイルを読み込む
    post = requests.post(url ,headers = headers ,params=payload,files=files)