import sys, os
sys.path.append('~/DjangoWeb/gensho')
sys.path.append('~/DjangoWeb')
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoWeb.settings'
import DjangoWeb.settings
import django
django.setup()

import json, twitter_conf
from requests_oauthlib import OAuth1Session
from gensho.models import Post

CK = twitter_conf.CONSUMER_KEY
CS = twitter_conf.CONSUMER_SECRET
AT = twitter_conf.ACCESS_TOKEN
ATS = twitter_conf.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)
url = "https://api.twitter.com/1.1/search/tweets.json"
params = {'q': '現象に名前 つけたい', 'count': 5, 'lang': 'ja'}
out_list = []
'''
source:(https://in-bee.net/media/articles/61)
'''
with open("ero.txt", 'r') as f:
    ero_data = f.read()
    for ero in ero_data:
        if ero != '\n':
            out_list.append(ero)

req = twitter.get(url, params=params)
search_timeline = json.loads(req.text)

if req.status_code == 200:
    for tweet in search_timeline['statuses']:
        if tweet['text'] not in out_list:
            t_user = tweet['user']['screen_name']
            t_text = tweet['text']
            b = Post(text=t_text, post_user=t_user)
            b.save()
else:
    print("ERROR: %d" % req.status_code)
