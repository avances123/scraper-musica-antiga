#!/usr/bin/python
import feedparser
from BeautifulSoup import BeautifulSoup
import re
import htmlentitydefs
import sys,os
import subprocess

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



def main(user,passwd,blogid = '8625828710657758692'):
   d = feedparser.parse('http://www.blogger.com/feeds/' + blogid + '/posts/default?max-results=1000000000')
   print 'http://www.blogger.com/feeds/' + blogid + '/posts/default?max-results=1000000000'
   for entry in d.entries:
       titulo = slugfy(entry.title,'-')
       print titulo
       html = entry.content[0].value
       soup = BeautifulSoup(html)
       enlaces = soup.findAll(href=re.compile("megaupload|rapidshare"))
       for enlace in enlaces:
           print "mkdir " + titulo
           subprocess.call(['mkdir',titulo])
           url = enlace['href']




if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    blogid = sys.argv[3]
    main(user,passwd,blogid)

