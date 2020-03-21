from login import * 
from requesting import *
import urllib.request
import requests
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import csv


driver = webdriver.Edge() #use edge
pixivUrl = "https://accounts.pixiv.net/login?" #url
driver.get(pixivUrl) #get in to web
loginPixiv(driver) #login
time.sleep(5) #delay

linkTail = [] #array of link tail to request to
count = 0 #how many bookmarks are there
for x in range (3):   # WORK IN PROGRESS

    userUrl ="https://www.pixiv.net/users/44700539/bookmarks/artworks?p="+str(x+1)
    driver.get(userUrl) #go to user
    time.sleep(5)
    page_html = driver.page_source  #get page source
    data = soup(page_html,"html.parser") #scan data
    if count == 0 :                                                 #find how many bms are there
        num = data.findAll('div',{"class":"sc-fzqzEs iPSfO"})
        count = num[0].findAll('span')
        print(count)
    
    bigFrame = data.findAll('ul',{"class":"_2WwRD0o _2WyzEUZ"}) #get big frame
    smallFrame = bigFrame[0].find_all('li',{"class":'_1Ed7xkM'}) #get small frame
    anchor = smallFrame[0].find_all('a') #get a tag
    print(len(smallFrame)) #print small frame, by default it will have 48
    print(len(anchor)) #get list of anchor tags(there are 2 pic-url and 2 illustrator-url) so the output should be 4
    print("_____________________________________")


#in the section below I scraped to get the link tail

    for i in range(len(smallFrame)):
        for a in smallFrame[i].find_all('a'):
            print(a['href'])
            linkTail.append(a['href']) #append link tail
            break #break cause there will be 4 links but we use only 1

#and on this section I am going to send a request and gets likes for each picture
bookmarks = getBookmarks(linkTail)

#?p=2 for viewing page 2
####################      D A T A     S E C T I O N      ###############################
#write data to csv file
with open("data.csv","w",newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Num","Bookmarks"])
    for i in range (len(bookmarks)):
        writer.writerow([i,bookmarks[i]])

