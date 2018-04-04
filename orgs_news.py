from utils import Crunchbase, tools
import requests
import json

#stopwords
from stop_words import get_stop_words
stop_words = get_stop_words('en')

#get our api key from the json file
key = json.load(open('api_key.json'))['newsfeed']

#----part 1: get the largest organizations----
companies = Crunchbase.get_big_companies()

#----part 2: recent news about them----

#a dictionary of dictionaries
word_list = {}

tld = 'com'
lang = 'en'
num = 5
start = 0
stop = 100 
pause = 3.0

import googlesearch
import urllib2
from bs4 import BeautifulSoup

words = {}

from stop_words import get_stop_words

stop_words = get_stop_words('en')
other_words = ['','\n','\t']

#companies = Crunchbase.get_big_companies()
companies = ["apple","samsung"]
for company in companies:
    query = company
    for pg in googlesearch.search(query, tld=tld, num=num, stop=stop, pause=pause):
        try:
            request = urllib2.Request(pg)
            #robot? who's a robot? not me
            request.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
            res = urllib2.urlopen(request)
            html = res.read()

            soup = BeautifulSoup(html, "html.parser")
            body = soup.find('body')
            c = tools.textify(''.join(['%s' % x for x in soup.body.findChildren()]))
    
            for word in c.split(" "):
                word = str(word)
                if word.lower() != query and '%' not in word and '\\' not in word and word not in other_words and word not in stop_words:
                    if word in words:
                        words[word] = words[word]+1
                    else:
                        words[word] = 1
        except:
            pass

words = tools.top_words(words, 10)
print words 
