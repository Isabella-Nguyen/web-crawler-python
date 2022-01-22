import urllib.request
import sys

#returns the string contents of the page at url, or "" if there is an error
def readurl(url):
	try:
		fp = urllib.request.urlopen(url)
		mybytes = fp.read()

		mystr = mybytes.decode(sys.stdout.encoding)
		fp.close()
		return mystr
	except:
		print("Failed to read")
		return ""
