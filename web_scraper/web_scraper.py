# Louis George
# Web Scraper

import numpy as np
import pandas as pd 
from time import sleep

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

class ScriptScraper():

    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\louis\Downloads\Chromedriver\chromedriver_win32\chromedriver.exe")

    def getit(self):

        self.movie_links = []
        self.movie_titles = []
        self.genre = []
        self.movie_script = []

        # Loads the page listing all movies
        self.driver.get("https://www.imsdb.com/all%20scripts/")

        # Find and get links to movies
        for i in self.driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[3]/p"):
            movie_links.append(i.find_element_by_xpath('.//a').get_attribute('href'))
            
            first_button = i.find_element_by_xpath('.//a')
            first_button.click()

            movie_title = self.driver.find_element_by_xpath('//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/table[1]/tbody/tr[1]/td/h1')

            if link_count > 1:
                break

    def no_loop_test(self):
        test_movie_titles = []
        test_genre = []
        test_movie_script = []
        # Loads the page listing all movies
        self.driver.get("https://www.imsdb.com/all%20scripts/")

        sleep(2)
        # gets movie title
        test_movie_titles.append(self.driver.find_element_by_xpath('//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/p[1]/a').get_attribute('text'))
        # moves to intermediate page
        first_button = self.driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[3]/p[1]/a")
        first_button.click()
        
        sleep(2)
        # moves to script page
        script_button = self.driver.find_element_by_xpath('//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/table[1]/tbody/tr[2]/td[2]/a[6]')
        script_button.click()

        sleep(2)
        # Gets script
        test_movie_script.append(self.driver.find_element_by_xpath('//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/table/tbody/tr/td/pre/pre').text)
        # Gets genre
        genre_inter = []
        for i in self.driver.find_elements_by_xpath('//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr/td[2]/a[contains(@href, "/genre")]'):
            genre_inter.append(i.get_attribute('text'))
        test_genre.append(genre_inter)

        return test_movie_titles, len(test_movie_script), test_genre

