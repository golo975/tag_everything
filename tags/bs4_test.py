from bs4 import BeautifulSoup

"https://www.jianshu.com/p/2b783f7914c6"

soup = BeautifulSoup('<html><body><p>data</p></body></html>')
print(soup)
print(soup('p'))
