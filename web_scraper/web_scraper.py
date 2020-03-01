# Louis George
# Web Scraper

import numpy as np
import pandas as pd 
from time import sleep

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class ScriptScraper():

    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\louis\Downloads\Chromedriver\chromedriver_win32\chromedriver.exe")

    def num_elements(self):

        self.movie_links = []
        self.movie_titles = []

        # Loads the page listing all movies
        self.driver.get("https://www.imsdb.com/all%20scripts/")

        # the wait code was copied from a kind soul on stack overflow @:
        # https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python 
        #####
        timeout = 10
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/table[2]/tbody/tr/td[3]/p'))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        #####
        print("I'm here")
        # Find and get links to movies
        for i in self.driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[3]/p"):
            self.movie_links.append(i.find_element_by_xpath('.//a').get_attribute('href'))
            self.movie_titles.append(i.find_element_by_xpath('.//a').get_attribute('text'))
            
    def gitit(self):

        for i in self.movie_links:
            pass



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

