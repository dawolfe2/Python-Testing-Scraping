from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def grab():
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get("<a href=""https://www.edureka.co/blog/web-scraping-with-python/")
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('a',href=True, attrs={'class': 'free-webinar-reg-box in hide-box'}):
        name = a.find('div', attrs={'class': 'webinar-box-title'})
        return(name)


if __name__ == '__main__':
    output = grab()
    print(output)