# Wikiracer

A python script to find the paths between given start and end wiki pages using the link on these pages.
The wikiShortPath Program finds the shortest path between the start and end pages.

### Requirements:
Written in Python 2.7

Packages: BeautifulSoup, urllib2, time.

### Algorithms:
The wikiPath program uses Breadth first Search traversal approach to find the path from given start page and end page. The result will be a list of paths from start page to end page.

Example Input: Book    Seattle

Example output: ['Book', 'Address_book', 'Telephone_directory', 'Seattle']

The wikiShortPath program uses Breadth first Search traversal with some pre-computation to find the shortest path between given start and end pages. The result will be a shortest path from start page to end page.

### Instructions to run:
python wikiPath.py
python wikiShortPath.py


