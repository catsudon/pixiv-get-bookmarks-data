pixivUser = "****YOUR EMAIL****"
pixivPassword = "****YOUR PASSWORD****"

import urllib.request
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def loginPixiv(browser):
    Username = browser.find_element_by_xpath("//*[@id='LoginComponent']/form/div[1]/div[1]/input")
    Username.send_keys(pixivUser) #input username
    Password = browser.find_element_by_xpath("//*[@id='LoginComponent']/form/div[1]/div[2]/input")
    Password.send_keys(pixivPassword) #input password
    Login = browser.find_elements_by_tag_name('button')[1]
    time.sleep(1)
    Login.click()

def getData(driver):
    picblock = driver.find_elements_by_class_name("bSWQGS")
    picblock[0].click()

def get_soup(browser):
    return soup(browser.page_source, 'html.parser')

def download_image(soup):
    url = soup.find_all('a', {'target': '_blank'})[1].get('href')
    print(url)

