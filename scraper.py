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



def main(user,passwd,blogid):
   d = feedparser.parse('http://www.blogger.com/feeds/' + blogid + '/posts/default?max-results=10')

   subprocess.call(['mkdir','-p',blogid])
   os.chdir(os.path.join(os.getcwd(),blogid))
   basedir = os.getcwd()
   for entry in d.entries:
       titulo = slugfy(entry.title,'-')
       html = entry.content[0].value
       soup = BeautifulSoup(html)
       enlaces = soup.findAll(href=re.compile("megaupload|rapidshare"))
       subprocess.call(['mkdir','-p',titulo])
       os.chdir(os.path.join(basedir,titulo))

       pretty_html = soup.prettify()
       output = open('info.html', 'wb')
       output.write(pretty_html)
       output.close()



       for enlace in enlaces:
           url = enlace['href']
	   subprocess.call(['plowdown','-a',user + ':' + passwd,url])
       os.chdir(basedir)




if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    blogid = '8625828710657758692'
    main(user,passwd,blogid)

