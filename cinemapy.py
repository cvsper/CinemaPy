 ##################################################                               
#	 _____  _                        _____      	#
#	|     ||_| ___  ___  _____  ___ |  _  | _ _ 	#
#	|   --|| ||   || -_||     || .'||   __|| | |	#
#	|_____||_||_|_||___||_|_|_||__,||__|   |_  |	#
#	                                       |___|	#
# ################################################# #

# requests for grabbing web pages
import requests
# BeautifulSoup for parsing web data
from bs4 import BeautifulSoup
# for opening video
from os import system
#for creating flasgs
import argparse

import recommend

"""
This will be a web scraper for movies url vexmovies.org
idk yet i may come back and make it a api for a site
or just push it to some website with flask who knows what the
future holds.
"""

# For adding flags we'll use argparser
parser= argparse.ArgumentParser(description='''CinemaPy:  Web scraper for watching streamed movies..''')
parser.add_argument('-m', '--movie', type=str, help=':List movie title')
parser.add_argument('-w', '--watch', type=bool, help=':To open movie in browser enter True')
parser.add_argument('-s', '--search', type=str, help=':Search and recieve a list of movies')
parser.add_argument('-y', '--year', type=int, help=':Enter a year and get a list of movies to watch from that year')
parser.add_argument('-g', '--genre', type=str, help=':List movies by genre')
parser.add_argument('-r', '--recommend', type=str, help=':List movie recommendations')

args = parser.parse_args()

class Genre:
	def __init__(self, cat):
		self.url = 'http://vexmovies.org/category/'
		self.cat = self.url + cat
		self.r = requests.get(self.cat)
	def get_genre(self):

		lists = []
		pages = raw_input('How many pages would you like to search? : ')
		for x in range(int(pages)):
			self.r = requests.get(self.url + str(x))
			try:
				self.soup = BeautifulSoup(self.r.content, 'lxml')
			except:
				self.soup = BeautifulSoup(self.r.content, 'html.parser')
			self.titles = self.soup.find_all('div',{'class':'item'})
			for title in self.titles:
				link = title.find_all('a')
				for x in link:
					print x.get('href')

#get list of movies by year
class yearList:
	def __init__(self, year):
		self.url = 'http://vexmovies.org/release-year/'
		self.url = self.url + year
		self.r = requests.get(self.url)

	def get_yr(self):
		try:
			self.soup = BeautifulSoup(self.r.content, 'lxml')
		except:
			self.soup = BeautifulSoup(self.r.content, 'html.parser')
		self.link = self.soup.find_all('a')
		return self.link

# This will loop threw every page and get the title 
class listAll:
	def __init__(self):
		self.url = 'http://vexmovies.org/page/'
		lists = []
		pages = raw_input('How many pages would you like to search? : ')
		for x in range(int(pages)):
			self.r = requests.get(self.url + str(x))
			try:
				self.soup = BeautifulSoup(self.r.content, 'lxml')
			except:
				self.soup = BeautifulSoup(self.r.content, 'html.parser')
			self.titles = self.soup.find_all('div',{'class':'item'})
			for title in self.titles:
				link = title.find_all('a')
				for x in link:
					print x.get('href')

	def get_titles(self):
		self.titles = self.soup.find_all('div',{'class':'item'})
		return self.titles
		system('open ', links[0])

# Return search results
class Search:
	def __init__(self):
		self.url = 'http://vexmovies.org/'
		self.url = self.url + '?s=' + args.search.replace(' ','+')
		self.r = requests.get(self.url)

	def search(self):
		try:
			self.soup = BeautifulSoup(self.r.content, 'lxml')
		except:
			self.soup = BeautifulSoup(self.r.content, 'html.parser')
		self.link = self.soup.find_all('div', {'class':'item'})
		for link in self.link:
			urls = link.find_all('a')
			for url in urls:
				print url.get('- ' + 'href')

	def title(self):
		try:
			self.soup = BeautifulSoup(self.r.content, 'lxml')
		except:
			self.soup = BeautifulSoup(self.r.content, 'html.parser')
		self.link = self.soup.find_all('div', {'class':'item'})
		for link in self.link:
			urls = link.find_all('img')
			for url in urls:
				print url.get('alt')

	def pages(self):
		try:
			self.soup = BeautifulSoup(self.r.content, 'lxml')
		except:
			self.soup = BeautifulSoup(self.r.content, 'html.parser')
		self.link = self.soup.find_all('a', {'class':'previouspostslink'})
		for link in self.link:
			self.urls = link.get('href')
			print self.urls	

def openVid(link):
	system('open ' + link)

def main():

	# The url that we will be scraping
	url = 'http://vexmovies.org/'

	# I want to be able to just type in a movie name so we'll use argsparser or raw_inpurt
	try:
		movie_title = args.movie.replace(' ', '-')
	except:
		movie_title = raw_input('Enter your movie title : ').replace(' ', '-')
	# concatinate the url and movie_title for the final url
	url = url + movie_title

	# now time to get the data with requests
	r = requests.get(url)

	# time to parse our data with soup
	# for some reason lxml doesnt work on every machine so we'll have
	# add a try and except, if lxml doesnt work will run html.parser instead
	try:
		soup = BeautifulSoup(r.content, 'lxml')
	except:
		soup = BeautifulSoup(r.content, 'html.parser')
	
	#now lets get
	link = soup.find_all('iframe')
	
	#also create a empty array to append results to
	links = []
	# loop threw the iframe to find the src url
	for src in link:
		links.append(src.get('src'))
	
	# print your results
	try:
		print('your preview link is : ' + links[1] + '\n')
	except IndexError:
		pass
	try:
		print('your video link is : ' + links[0])
	except IndexError:
		print("Title was not found")		
	if args.watch == True:
		openVid(links[0])

if __name__ == '__main__':
	if args.search:
		s = Search()
		title = s.title()
		print('================'+ 'MOVIE RECOMMENDATIONS'+'===============')
		recommend.movie(args.search)
		print('================'+ 'TV SHOW RECOMMENDATIONS'+'===============')
		recommend.shows(args.search)
	elif args.recommend:
		recommend.main(args.recommend)	
	else:	
		main()