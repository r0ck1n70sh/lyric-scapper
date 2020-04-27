import requests
from bs4 import BeautifulSoup

qry= input("Enter Lyrics:")
#print(qry)

qry= qry.lower()
str=""
for c in qry:
	asc= ord(c)
	#print(asc, end=' ')

	if(asc==32):
		str+= '+'
	elif(asc>=97 and asc<=122):
		str+= c
	else:
		str+= ('%'+hex(asc).lstrip("0x").upper())

#print(str)

URL= "https://search.azlyrics.com/search.php?q="
URL+= str

page= requests.get(URL)
content= BeautifulSoup(page.content, 'html.parser')

td_elems= content.find_all('td', class_ ="text-left visitedlyr")

srch= []
for elem in td_elems:
	curr= {}
	curr['link']= elem.a['href']

	text= elem.find_all('b')
	curr['name']=text[0].text
	curr['artist']= text[1].text

	srch.append(curr)

print(srch)


