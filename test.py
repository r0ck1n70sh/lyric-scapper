import requests
from bs4 import BeautifulSoup

url = "https://search.azlyrics.com/search.php?q=smoke+weed+everyday"
page= requests.get(url)

content= BeautifulSoup(page.content , 'html.parser')

td_elems= content.find_all('td', class_= "text-left visitedlyr")

#f= file.open('out', 'w')
for elem in td_elems:
	link_href= elem.a['href']
	text= elem.find_all('b')
	for str in text:
		print(str.text, end="||")
	
	print(link_href)
	




