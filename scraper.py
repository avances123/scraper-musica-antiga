import feedparser
from BeautifulSoup import BeautifulSoup
import re


# GET http://www.blogger.com/feeds/blogID/posts/default?max-results=26


d = feedparser.parse('http://www.blogger.com/feeds/8625828710657758692/posts/default?max-results=1')

for entry in d.entries:
    html = entry.content[0].value
    soup = BeautifulSoup(html)
    #print soup.prettify()
    enlaces = soup.findAll(href=re.compile("megaupload|rapidshare"))
    for enlace in enlaces:
    	print enlace['href']


