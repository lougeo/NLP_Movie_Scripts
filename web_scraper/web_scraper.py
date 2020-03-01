# Louis George
# Web Scraper

import numpy as np
import pandas as pd 
from time import sleep

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
            
            first_button = i.find_element_by_xpath('.//a')
            first_button.click()

            movie_title = self.driver.find_element_by_xpath('//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/table[1]/tbody/tr[1]/td/h1')

            if link_count > 1:
                break

    def no_loop_test(self):
        movie_titles = []
        movie_script = []
        # Loads the page listing all movies
        self.driver.get("https://www.imsdb.com/all%20scripts/")

        sleep(2)
        
        movie_titles.append(self.driver.find_element_by_xpath('//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/p[1]/a').get_attribute('title'))

        first_button = self.driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[3]/p[1]/a")
        first_button.click()
        
        sleep(2)

        script_button = self.driver.find_element_by_xpath('//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/table[1]/tbody/tr[2]/td[2]/a[6]')
        script_button.click()

        sleep(2)

        movie_script.append(self.driver.find_element_by_xpath('//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/table/tbody/tr/td/pre/pre').text)

        return movie_titles, len(movie_script)

