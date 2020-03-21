import requests
from bs4 import BeautifulSoup as soup
import json

def getBookmarks(linkTail):
    bookmarks = []
    for i in range(len(linkTail)):
        picnum = linkTail[i][13:len(linkTail[i])]#get only the pic number
        # print(picnum)
        url = "https://www.pixiv.net"+linkTail[i] #get full link
        dataUrl = requests.get(url) #request to that link
        dataWeGot = soup(dataUrl.text,'html.parser') #parse data we got
        # print(dataWeGot)
        a = dataWeGot.findAll("meta") #find bookmark section
        content = a[25]['content']
        content = json.loads(content) #convert string into json
        bookmarks.append(content['illust'][picnum]['bookmarkCount']) #bookmark's path on JSON
        print((content['illust'][picnum]['bookmarkCount']))

    return bookmarks






#############     L A B    S E C T I O N        #######################
# linkTail = ["/en/artworks/64698566","/en/artworks/75726769"]

# getBookmarks(linkTail)