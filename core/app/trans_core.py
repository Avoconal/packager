import requests
import random
from hashlib import md5

appid = '20220715001273937'
appkey = 'y1YW1AS69iDH73PuQVgn'
cout=0


def get(txt: str):
    global cout
    cout+=1
    if txt[0].lower() in 'abcdefghijklmnopqrstuvwxyz':
        from_lang, to_lang = 'en', 'zh'
    else:
        from_lang, to_lang = 'zh', 'en'

    salt = random.randint(32768, 65536)
    params = {'appid': appid, 'q': txt, 'from': from_lang, 'to': to_lang, 'salt': salt,
              'sign': md5(str(appid + txt + str(salt) + appkey).encode('utf-8')).hexdigest()}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    result=requests.post('http://api.fanyi.baidu.com/api/trans/vip/translate', params=params, headers=headers).json()['trans_result']
    print('send a request({})：{}'.format(cout,str(txt+' '*25)[:25].replace('\n',' ')))
    return [temp['dst'] for temp in result]

