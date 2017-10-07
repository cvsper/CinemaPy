import requests
from bs4 import BeautifulSoup as BS

def movie(search):
	url = 'https://tastedive.com/movies/like/' + search
	r = requests.get(url)
	soup = BS(r.content, 'lxml')
	links = soup.find_all('span',{'class':'tk-Resource-title'})
	for link in links:
		print('- ' + link.text)

def shows(search):
	url = 'https://tastedive.com/shows/like/' + search
	r = requests.get(url)
	soup = BS(r.content, 'lxml')
	links = soup.find_all('span',{'class':'tk-Resource-title'})
	for link in links:
		print('- ' + link.text)