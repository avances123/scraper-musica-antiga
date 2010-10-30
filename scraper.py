import feedparser

# GET http://www.blogger.com/feeds/blogID/posts/default?max-results=26


d = feedparser.parse('http://www.blogger.com/feeds/8625828710657758692/posts/default?max-results=10000000')

print str(len(d.entries))

