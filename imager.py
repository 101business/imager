from selenium import webdriver
from time import sleep


class Imager():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://unsplash.com/s/photos/'+keyword[i])

        sleep(2)

        image1 = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[3]/div[4]/div/div/div/div[1]/figure[1]/div/div[1]/div/div/a/div/div[2]/div/img')
        image1.click()

        sleep(2)

        dl = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[4]/div/div/div[1]/div[1]/header/div[2]/div[3]/div/a/span')
        dl.click()

        sleep(2)


keyword = ('cheese','milk','camera')

for i in range(0,len(keyword)):
    bot = Imager()
    bot.driver.quit()
