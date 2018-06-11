from bs4 import BeautifulSoup
import urllib2
import time

'''
This program finds the path between given
start page and end page. 
'''

class WikiRacer:
	def __init__(self,startPage,endPage):
		self.startPage = startPage
		self.endPage = endPage
		self.startPageLink = self.createPageAddress(startPage)
		self.endPageLink = self.createPageAddress(endPage)
		self.paths = {startPage:[startPage]}
		self.queue = [startPage]

	def Path(self):
		while len(self.queue):
			#pop from queue
			currentPageTitle = self.queue.pop(0)

			#find the links of popped page
			currentPageLinks = self.getWikiLinks(currentPageTitle)

			#check for exceptions
			if currentPageLinks == None:
				return None

			# check if endPage is in currentPageLinks
			if self.endPage in currentPageLinks:
				return self.paths[currentPageTitle]+[self.endPage]

			else:
				for neighbour in currentPageLinks:
					if neighbour not in self.paths[currentPageTitle]:
						self.queue.append(neighbour)
						self.paths[neighbour] = self.paths[currentPageTitle]+[neighbour]
						#print neighbour


	# create http link for given PageTitle
	def createPageAddress(self,PageTitle):
		return "https://en.wikipedia.org/wiki/"+str(PageTitle)


	# get all links from the page
	def getWikiLinks(self,page):
		pageaddress = self.createPageAddress(page)
		#print pageaddress
		try:
			resp = urllib2.urlopen(pageaddress)
		except urllib2.HTTPError, e:
			print "Please enter correct Page Name"
			return None
		soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
		links_on_page = set()
		for link in soup.find_all('a', href=True):
			if "/wiki/" in str(link) and ":" not in str(link):
				link_split = str(link['href'].encode('ascii', 'ignore')).split("/wiki/")
				links_on_page.add(str(link_split[1]))
		return list(links_on_page)



startPage = raw_input("Please enter Start Page Title: ")
endPage = raw_input("Please enter End Page Title: ")

start_time = time.time()
racer = WikiRacer(str(startPage),str(endPage))
print racer.Path()
print("--- %s seconds ---" % (time.time() - start_time))