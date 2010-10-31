import feedparser
from BeautifulSoup import BeautifulSoup
import re
import htmlentitydefs, re

def slugfy(text, separator):
    ret = ""
    for c in text.lower():
        try:
	    ret += htmlentitydefs.codepoint2name[ord(c)]
	except:
	    ret += c

    ret = re.sub("([a-zA-Z])(uml|acute|grave|circ|tilde|cedil)", r"\1", ret)
    ret = re.sub("\W", " ", ret)
    ret = re.sub(" +", separator, ret)
    return ret.strip()


# GET http://www.blogger.com/feeds/blogID/posts/default?max-results=26


d = feedparser.parse('http://www.blogger.com/feeds/8625828710657758692/posts/default?max-results=1000000000')

for entry in d.entries:
    titulo = slugfy(entry.title,'-')
    html = entry.content[0].value
    soup = BeautifulSoup(html)
    enlaces = soup.findAll(href=re.compile("megaupload|rapidshare"))
    for enlace in enlaces:
    	print enlace['href']



