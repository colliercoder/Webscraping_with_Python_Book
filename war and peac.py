from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html,'lxml')

nameList = bs.findAll("span",class_={"green","red"}) #bsObj.findAll(tagName, tagAttributes)
count_prince = bs.find_all(text="the prince")
print(len(count_prince))
title = bs.find(id='title')
print(title)
for name in nameList:
    print(name.get_text()) #get_text() strips all the tags away and just supplies the texr

"""
The two functions are extremely similar, as evidenced by their definitions in the
BeautifulSoup documentation:

findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)

95% of the time only going to be needing 'tag' and 'attributes'
"""