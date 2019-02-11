# coding: utf-8

from requests_oauthlib import OAuth1Session
import urllib.request
from getdog import Getdog
import json
api="GHCWWtbSJELuVaczJgk5ERm8k" #API key
api_secret="f4mqv7WdIWEpnKE7G05WtecsctqTh0Q9sjFLLrhyE6ytXKKYw8" #API secret key
token="1094778328177758208-4pfCGuR7M9geIA5LDHOpso0IY2JibW" #Access token
token_secret="2sWl0zjJtveNKkTq4GjWcJTfXlLu3D3iogFXcbmlfs1WC" #Access token secret
url = "https://api.twitter.com/1.1/statuses/update.json"

txt=Getdog().getitems()
weburl=Getdog().url

#OAuth認証で POST method で投稿
twitter = OAuth1Session(api,api_secret,token,token_secret)

url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

for i in txt:

    # 画像投稿
    iurl="http://www.aomori-animal.jp/02_JOTO/INU"+i[4].lstrip(".")
    response=urllib.request.urlopen(iurl)
    img=response.read()
    files = {"media" : img}
    req_media = twitter.post(url_media, files = files)

    # レスポンスを確認
    if req_media.status_code != 200:
        print ("img update failed: %s", req_media.text)
        exit()

    # Media ID を取得
    media_id = json.loads(req_media.text)['media_id']
    print ("Media ID: %d" % media_id)

    # Media ID を付加してテキストを投稿
    message=i[0]+","+i[1]+","+i[2]+"\r"+i[3]+"\r"+weburl
    params = {'status': message, "media_ids": [media_id]}
    req_media = twitter.post(url_text, params = params)

    if req_media.status_code != 200:
        print ("txt update failed: %s", req_text.text)
        exit()

    

 


