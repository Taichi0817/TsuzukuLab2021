import requests

def line_notify(message='演算終了'):
    line_notify_token = 'akHLNAuC8XmSHLXRuOMChlMe3FpfmU2E8KoWXzf21wL'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)