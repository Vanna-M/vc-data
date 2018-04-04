import requests, json, googlesearch, urllib2
from utils import tools
from bs4 import BeautifulSoup
from stop_words import get_stop_words
stop_words = get_stop_words('en')

#each list is in diff format, needs own search
#where to get data
import os
directory = os.path.dirname(__file__)
folder = "utils/data/"

#----midas list 2015----
m15 =  open(os.path.join(directory,"%sMidas2015.html"%folder),"r")
#beautifulsoup makes life better
soup = BeautifulSoup(m15,"html.parser")

people15 = []
vcs15 = []

track = 0
for div in soup.body.findAll('div'):
    if div.text.isdigit():
        track = 1
    elif track == 1:
        people15.append(div.text)
        track = 2
    elif track == 2:
        vcs15.append(div.text)
        track = 0

#----midas list 2016----
m16 = open(os.path.join(directory,"%sMidas2016.html"%folder),"r")
soup = BeautifulSoup(m16,"html.parser")
people16 = []
vcs16 = []

from string import ascii_letters
body = soup.body.findAll('p')
for p in body:
    if "overall ranking" in str(p):
        for line in str(p).split("\n"):
            name = ""
            co = ""
            
            i = 0
            #names + company 
            for letter in line:
                letter = str(letter)
                if i == 0:
                    if letter == " ":
                        i+=1
                elif i == 1:
                    if letter not in ascii_letters+' ':
                        i += 1
                    else:
                        name += letter
                else:
                    if letter == "<":
                        break 
                    else:
                        co += letter
            #formatting
            name = name.strip()
            co = co[2:].strip()
            people16.append(name)
            vcs16.append(co)

#formatting
people16 = people16[1:]
vcs16 = vcs16[1:]

#----midas list 2017----
m17 = open(os.path.join(directory,"%sMidas2017.html"%folder),"r")
soup = BeautifulSoup(m17,"html.parser")
people17 = []
vcs17 = []

import re
body = soup.body.findAll('h3')
for h3 in body:
    name = h3.find('a').text
    people17.append(name)

pattern = re.compile(r"Firm")
body = soup.body.findAll(text=pattern)
for i in body:
    co = i.parent.parent.text[5:].strip()
    vcs17.append(co)

#----midas list 2018----
m18 = open(os.path.join(directory,"%sMidas2018.html"%folder),"r")
soup = BeautifulSoup(m18,"html.parser")
people18 = []
vcs18 = []

people = {}
vcs = {}
qualify = {}

for person in soup.body.findAll('p',class_='p19'):
        people18.append(person.text)
for company in soup.body.findAll('p',class_='p20'):
    vcs18.append(company.text)

#close it all up, we're done
m15.close()
m16.close()
m17.close()
m18.close()


#-----analysis begins------
people = {}
vcs = {}

people = tools.addAll(people,people15,'2015')
people = tools.addAll(people,people16,'2016')
people = tools.addAll(people,people17,'2017')
people = tools.addAll(people,people18,'2018')

vcs = tools.addAll(vcs,vcs15,'2015')
vcs = tools.addAll(vcs,vcs16,'2016')
vcs = tools.addAll(vcs,vcs17,'2017')
vcs = tools.addAll(vcs,vcs18,'2018')

repeatPeople = [0 for x in range(4)]
repeatVcs = [0 for x in range(4)]

for person in people:
    repeatPeople[len(people[person])-1]+=1

for vc in vcs:
    repeatVcs[len(vcs[vc])-1]+=1

print "repeat people"
print repeatPeople
repeatPeoplePercents = [(x*1.0/sum(repeatPeople))*100 for x in repeatPeople]
print repeatPeoplePercents

print "repeat vcs"
print repeatVcs
repeatCompaniesPercents = [(x*1.0/sum(repeatVcs))*100 for x in repeatVcs]
print repeatCompaniesPercents

import facebook
access_token = 'EAACEdEose0cBAPHHmPCccQTAYeNL80ioPTeXFxIOvHBoUzm4wYG1DdwUE4ZCqk2cykadzQn3uHAC0R9wrUlnmXZA8XmHdtphs5qH3yNhYZBOinoYUaz1mrxUGxaEigBtKOC0v7ImhKVZAWHI57K6eOK0xEkXHw9shsamTY1jXYqNiwzfhXE1yyyrTOl3U1bZBFyik4UZCs3wZDZD'

def get_message(post):
    print(post['message'])


messages = []

from stop_words import get_stop_words

stop_words = get_stop_words('en')
other_words = ['','\n','\t']

import wikipedia
words = ""
failed = []

for person in people:
    try: 
        words += wikipedia.summary(person)
    except:
        failed.append(person)

print "%d vcs have no info"%len(failed)
print tools.top_words(words,10)
words = []


for person in people15:
    try: 
        words += wikipedia.summary(person)
    except:
        failed.append(person)

print tools.top_words(words,10)
words = []

for person in people16:
    try: 
        words += wikipedia.summary(person)
    except:
        failed.append(person)

    
print tools.top_words(words,10)
words = []

for person in people17:
    try: 
        words += wikipedia.summary(person)
    except:
        failed.append(person)


print tools.top_words(words,10)

words = []

for person in people18:
    try: 
        words += wikipedia.summary(person)
    except:
        failed.append(person)

print tools.top_words(words,10)
