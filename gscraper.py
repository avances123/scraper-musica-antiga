import gdata.blogger.client
import gdata.client
import gdata.sample_util
import gdata.data
import atom.data



#def PrintAllPosts(blogger_service, blog_id):
#    	feed = blogger_service.GetFeed('/feeds/' + blog_id + '/posts/default')
#    	print feed.title.text
#	for entry in feed.entry:
#		print "\t" + entry.title.text
#		print "\t" + entry.content.text
#		print "\t" + entry.updated.text
#		print
#


def PrintAllPosts():
	"""
	This method displays the titles of all the posts in a blog.  First it
	requests the posts feed for the blogs and then it prints the results.
	"""

	# create client
	client = gdata.blogger.client.BloggerClient()
	
	# Request the feed.
	feed = client.get_posts('8625828710657758692')

	# Print the results.
	print feed.title.text
	print 'longitud entries:' + str(len(feed.entry))
	for entry in feed.entry:
		if not entry.title.text:
			print "\tNo Title"
		else:
			print "\t" + entry.title.text.encode('utf-8')
		print



def main():
	PrintAllPosts()

if __name__ == '__main__':
	main()


