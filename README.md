# Wikiracer

A python script to find the paths between given start and end wiki pages using the link on these pages.
The wikiShortPath Program finds the shortest path between the start and end pages.

### Requirements:
Written in Python 2.7

Packages: BeautifulSoup, urllib2, time.

### Algorithms:
The wikiPath program uses Breadth first Search traversal approach to find the path from given start page and end page. The result will be a list of paths from start page to end page.

Example Input: StartPage: Nicky_Kuiper     EndPage: Malaria

Example output: ['Nicky_Kuiper', 'SV_TEC', 'Netherlands_national_under-21_football_team', 'Feyenoord', 'FC_Eindhoven', 'Defender_(association_football)', 'Main_Page', 'Gian_Gastone_de%27_Medici,_Grand_Duke_of_Tuscany', 'Cosimo_I_de%27_Medici,_Grand_Duke_of_Tuscany', 'Malaria']

The wikiShortPath program uses Breadth first Search traversal with some pre-computation to find the shortest path between given start and end pages. The result will be a shortest path from start page to end page.

Example Input: StartPage: Nicky_Kuiper     EndPage: Malaria

Example output: ['Nicky_Kuiper', 'Association_football', 'Africa', 'Malnutrition', 'Malaria']


### Instructions to run:
python wikiPath.py

python wikiShortPath.py


