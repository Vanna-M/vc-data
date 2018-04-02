#mods
import urllib2
from bs4 import BeautifulSoup

#top organizations
pg = "https://www.crunchbase.com/search/organization.companies"
#the request
request = urllib2.Request(pg)
#robot? who's a robot? not me
request.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
#res = urllib2.urlopen(request)
#html = res.read()        

print html
'''
#beautiful soup
soup = BeautifulSoup(prs_org, "html.parser")

name_orgs = soup.find("div",{"class":"ng-star-inserted"})
print name_orgs.text
'''
