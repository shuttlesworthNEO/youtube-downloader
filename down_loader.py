import requests
from bs4 import BeautifulSoup
import os
import sys
import re

base_url='https://www.youtube.com'
url="https://www.youtube.com/results?search_query="

no_of_args = len(sys.argv)
arguments = str(sys.argv)
  
if arguments[1] == '-v' or arguments[-1] == '-m':
	query = '+'.join(arguments[2:])
else:
	query = '+'.join(arguments[1:])

youtube_r = requests.get(url+query)
youtube_soup = BeautifulSoup(youtube_r.text,'html.parser')

video_links = []

for link in youtube_soup.findAll('a'):
	if re.findall('^/watch?.+', link.get('href')):
		video_links.append(link.get('href'))

download_url = base_url+video_links[0]

if arguments[1] == '-m':
	os.system('youtube-dl --extract-audio --audio-format mp3 '+ download_url)
else:
	os.system('youtube-dl '+download_url) 	