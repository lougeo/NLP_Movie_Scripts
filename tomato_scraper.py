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

    def scores(self):

        movie_info = []
        # Split into two batches as only 1000 requests aloud per day
        titles = pd.read_csv('../movie_titles.csv').drop('Unnamed: 0', axis=1)
        titles1 = titles.iloc[:500, :]
        titles2 = titles.iloc[500:, :]

        for i in titles['titles']:
            try:
                self.driver.get(f'http://www.omdbapi.com/?apikey=fd40c3c8&t={i}')

                # Wait
                try:
                    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/pre'))
                    WebDriverWait(self.driver, timeout).until(element_present)
                except TimeoutException:
                    print("Timed out waiting for page to load")
                
                # Appending full json to list
                movie_info.append(self.driver.find_element_by_xpath('/html/body/pre').text)
            
            except:
                # Appends nan if timeout
                movie_info.append(np.nan)
    