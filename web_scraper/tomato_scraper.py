# Louis George
# API scraper for:
# omdbapi.com as of Feb 2020

import numpy as np
import pandas as pd 
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ScoreScraper():

    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\louis\Downloads\Chromedriver\chromedriver_win32\chromedriver.exe")

    def tables(self):

        # Split into two batches as only 1000 requests aloud per day
        titles = pd.read_csv('movie_titles.csv').drop('Unnamed: 0', axis=1)
        self.titles1 = titles.iloc[:500, :]
        self.titles2 = titles.iloc[500:, :]

    def getit1(self):
        timeout = 10
        self.movie_info1 = []
        self.movie_title_dyn1 = []

        for i in self.titles1['titles']:
            try:
                self.driver.get(f'http://www.omdbapi.com/?apikey=fd40c3c8&t={i}')
            
                # Wait
                try:
                    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/pre'))
                    WebDriverWait(self.driver, timeout).until(element_present)
                except TimeoutException:
                    print("Timed out waiting for page to load")
                
                # Appends movie title dynamically for reference
                self.movie_title_dyn1.append(i)
                # Appending full json to list
                self.movie_info1.append(self.driver.find_element_by_xpath('/html/body/pre').text)
            
            except:
                # Appends nan if timeout
                self.movie_info1.append(np.nan)

        df_movie_info1 = pd.DataFrame({'titles':self.movie_title_dyn1, 
                                       'info':self.movie_info1})
        df_movie_info1.to_csv('movie_info1.csv')
    
    def getit2(self):
        timeout = 10
        self.movie_info2 = []
        self.movie_title_dyn2 = []

        for i in self.titles2['titles']:
            try:
                self.driver.get(f'http://www.omdbapi.com/?apikey=fd40c3c8&t={i}')
            
                # Wait
                try:
                    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/pre'))
                    WebDriverWait(self.driver, timeout).until(element_present)
                except TimeoutException:
                    print("Timed out waiting for page to load")
                
                # Appends movie title dynamically for reference
                self.movie_title_dyn2.append(i)
                # Appending full json to list
                self.movie_info2.append(self.driver.find_element_by_xpath('/html/body/pre').text)
            
            except:
                # Appends nan if timeout
                self.movie_info2.append(np.nan)

        df_movie_info1 = pd.DataFrame({'titles':self.movie_title_dyn2, 
                                       'info':self.movie_info2})
        df_movie_info1.to_csv('movie_info2.csv')