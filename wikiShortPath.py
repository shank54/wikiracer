from bs4 import BeautifulSoup
import urllib2
from heapq import *
import time

'''
This program finds the shortest path
between the given start page and end page.
'''

class WikiRacer:
	def __init__(self,startPage,endPage):
		self.startPage = startPage
		self.endPage = endPage
		self.startPageLink = self.createPageAddress(startPage)
		self.endPageLink = self.createPageAddress(endPage)
		self.endPageLinks  = self.getWikiLinks(endPage)
		self.enddict = dict()

		#dict of endPageLinks for fast access.
		for page in self.endPageLinks:
			if str(page) not in self.enddict:
				self.enddict[str(page)] = 1
		self.paths = {startPage:[startPage]}
		self.tempdict = {startPage:self.getWikiLinks(startPage)}
		self.bfsqueue = [(1,startPage)]


	# BFS with some precomputation usin Priority Queue
	def minimumDistance(self):
		
		while len(self.bfsqueue):

			#pop from PriorityQueue
			priorityNumber,currentPageTitle = self.bfsqueue.pop(0)
			print currentPageTitle
			
			#find the links of popped page
			currentPageLinks = self.tempdict[currentPageTitle]
			#print currentPageLinks

			#check for exceptions
			if currentPageLinks == None:
				return None

			pqueue = []
			# check if endPage is in currentPageLinks
			if self.endPage in currentPageLinks:
				return self.paths[currentPageTitle]+[self.endPage]

			else:
				for neighbour in currentPageLinks:
					if neighbour not in self.paths[currentPageTitle]:
						#get priority number of neighbour with endpage
						priorityNumber = self.getPriority(neighbour)
						#print priorityNumber
						heappush(pqueue,(priorityNumber,neighbour))
						self.paths[neighbour] = self.paths[currentPageTitle]+[neighbour]
						#print neighbour
				self.bfsqueue.append(heappop(pqueue))


	# create http link for title
	def createPageAddress(self,PageTitle):
		return "https://en.wikipedia.org/wiki/"+str(PageTitle)

	def getPriority(self,givenPage):
		#links common between givenPage and endPage
		#print givenPage
		givenPageLinks = self.getWikiLinks(givenPage)
		if givenPageLinks == None:
			return 0
		self.tempdict[str(givenPage)] = givenPageLinks
		common = 0
		for page in givenPageLinks:
			if str(page) in self.enddict:
				common += 1
		return (-1)*common

	# get all links from the page
	def getWikiLinks(self,page):
		#print page
		pageaddress = self.createPageAddress(page)
		#print pageaddress
		resp = None
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
print racer.minimumDistance()
print("--- %s seconds ---" % (time.time() - start_time))