from requests_oauthlib import OAuth1Session
from datetime import datetime
import os.path
import urllib.request
import json
import configparser
import errno

config_ini = configparser.ConfigParser()
config_ini_path = 'config/config.ini'

if not os.path.exists(config_ini_path):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_ini_path)

config_ini.read(config_ini_path, encoding='utf-8')
read_default = config_ini['DEFAULT']

user_id = read_default.get('USER_ID')
CONSUMER_KEY = read_default.get('CONSUMER_KEY')
CONSUMER_SECRET = read_default.get('CONSUMER_SECRET')
ACCESS_TOKEN = read_default.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = read_default.get('ACCESS_TOKEN_SECRET')

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def get_fav_list():
    url = "https://api.twitter.com/1.1/favorites/list.json"
    params = {'user_id':user_id, 'count':5}
    response = twitter.get(url, params=params)
    if response.status_code == 200:
        r = json.loads(response.text)

        for i, tweet in enumerate(reversed(r)):
            user_object = tweet['user']
            text_object = tweet['text']
            #動画URLの初期設定
            video_url = ""
            #画像URLの初期設定
            image_urls = []
            #ツイートurlの初期設定
            tweet_url = ""
            print(user_object, text_object)

get_fav_list()