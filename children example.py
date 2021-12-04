from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html,'html.parser')
#bs = BeautifulSoup(html,'lxml')
#bs = BeautifulSoup(html,'html5lib')

for child in bs.find('table',{'id':'giftList'}).children:
    print(child)

print("---------------------------------------------------------------------------")

for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)

print("---------------------------------------------------------------------------")

print(bs.find('img',
              {'src':'../img/gifts/img1.jpg'})
      .parent.previous_sibling.get_text())

print("-----------------------------------------------------------------")

images = bs.find_all('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])