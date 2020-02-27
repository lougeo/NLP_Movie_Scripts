# Louis George
# Web Scraper

import numpy as np
import pandas as pd 

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

class ScriptScraper():

    movie_links = []
    link_count = 0

    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\louis\Downloads\Chromedriver\chromedriver_win32\chromedriver.exe")

    def num_elements(self):
        # Loads the page listing all movies
        self.driver.get("https://www.imsdb.com/all%20scripts/")
        # Find and get links to movies
        for i in self.driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[3]/p"):
            link_count += 1
            movie_links.append(i.find_element_by_xpath('.//a').get_attribute('href'))
    
    def gather(self):
        pass