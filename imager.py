from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time




class Imager():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://unsplash.com/s/photos/'+ keywords[i]) 


        image1 = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[3]/div[4]/div/div/div/div[1]/figure[1]/div/div[1]/div/div/a/div/div[2]/div/img')
        image1.click()

        sleep(3)

        dl = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[4]/div/div/div[1]/div[1]/header/div[2]/div[3]/div/a/span')
        dl.click()

        sleep(3)

        self.driver.get('https://unsplash.com/s/photos/'+ keywords[i]) 
        
        image2 = self.driver.find_element_by_xpath('')
        image2.click()

        sleep(3)

        dl = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[4]/div/div/div[1]/div[1]/header/div[2]/div[3]/div/a/span')
        dl.click()

        sleep(3)

        self.driver.get('https://unsplash.com/s/photos/'+ keywords[i]) 
        
        image3 = self.driver.find_element_by_xpath('')
        image3.click()

        sleep(3)

        dl = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[4]/div/div/div[1]/div[1]/header/div[2]/div[3]/div/a/span')
        dl.click()



'''
    case = self.driver.find_element_by_xpath('-----')
    email_in.send_keys(url[i])

    dw = self.driver.find_element_by_xpath('-----')
    dw.click()
    
    '''

keywords = ['ice', 'fun', 'motor']

for (i <= len(keywords)):
    bot = Imager()

