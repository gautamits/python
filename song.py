import urllib
import json as m_json
import bs4
import BeautifulSoup
#query = raw_input ( 'Query: ' )
query="chann+warga+mp3+download"
resp = urllib.urlopen ( "http://www.google.co.in/search?q=" + query ).read()
soup = bs4.BeautifulSoup(resp)
for line in soup.find_all('a'):
        print(line.get('href'))

"""
>>> mp3file = urllib.urlopen("http://dl2.yoyodesi.com/hd.yoyodesi.com/320/471325/Chann+Warga+-+Harjot%20(DJJOhAL.Com).mp3")
>>> with open('test.mp3','wb') as output:
...     output.write(mp3file.read())
"""