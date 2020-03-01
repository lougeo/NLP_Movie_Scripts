# Louis George
# Web Scraper for:
# IMSDb.com as of Feb 2020

import numpy as np
import pandas as pd 
from time import sleep

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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
    
        # Find and get links to movies
        for i in self.driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[3]/p"):
            self.movie_links.append(i.find_element_by_xpath('.//a').get_attribute('href'))
            self.movie_titles.append(i.find_element_by_xpath('.//a').get_attribute('text'))

#################################################
# WARNING: THIS FUNCTION RUNS FOR A LONG TIME 
#################################################
    def getit(self):
        count = 0
        self.movie_links = []
        self.movie_titles = []
        self.movie_scripts = []
        self.movie_genres = []
        self.movie_titles_dyn = []

        
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
    

        # Find and get links to movies
        for i in self.driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[3]/p"):
            self.movie_links.append(i.find_element_by_xpath('.//a').get_attribute('href'))
            self.movie_titles.append(i.find_element_by_xpath('.//a').get_attribute('text'))
        
        num_films = len(self.movie_links)
        print('All links found', end='\r')

        # Loops over all of the movie links collected with the num_elements function,
        # collecting the scripts, and genres, for each movie.
        for i in self.movie_links:

            # Dynamically update movie titles in case of crash/debugging purposes
            # Must come before count is updated
            self.movie_titles_dyn.append(self.movie_titles[count])

            # local variables
            timeout = 20
            count += 1

            # testing condition
            #if count > 3:
            #    break

            # Load intermediate page
            self.driver.get(i)

            # Wait
            try:
                element_present = EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/scripts")]'))
                WebDriverWait(self.driver, timeout).until(element_present)
            except TimeoutException:
                print("Timed out waiting for page to load")
            
            # Gets Genres
            # Changed so that it is more general
            # Downside is that it now picks up the 18 genres + the film genres
            # Easy enough to deal with in post
            genre_inter = []
            try:
                for i in self.driver.find_elements_by_xpath('//a[contains(@href, "/genre")]'):
                    genre_inter.append(i.get_attribute('text'))
                self.movie_genres.append(genre_inter)
            except NoSuchElementException:
                self.movie_genres.append(np.nan)

            # Load script page
            try:
                script_button = self.driver.find_element_by_xpath('//a[contains(@href, "/scripts")]')
                script_button.click()

                # Wait
                try:
                    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'scrtext'))
                    WebDriverWait(self.driver, timeout).until(element_present)
                except TimeoutException:
                    print("Timed out waiting for page to load")

                # Gets script
                self.movie_scripts.append(self.driver.find_element_by_class_name('scrtext').text)
            except NoSuchElementException:
                self.movie_scripts.append(np.nan)
            
            # Condition which saves progress as a csv every 100 scripts, and a final copy
            if count == num_films:
                df = pd.DataFrame({'titles':self.movie_titles_dyn,
                                   'scripts':self.movie_scripts,
                                   'genres':self.movie_genres})
                df.to_csv(f'scripts_upto_all.csv')
            elif (count % 100) == 0:
                df = pd.DataFrame({'titles':self.movie_titles_dyn,
                                   'scripts':self.movie_scripts,
                                   'genres':self.movie_genres})
                df.to_csv(f'scripts_upto_{count}.csv')
            # Test condition
            #elif count == 3:
            #    df = pd.DataFrame({'titles':self.movie_titles_dyn,
            #                       'scripts':self.movie_scripts,
            #                       'genres':self.movie_genres})
            #    df.to_csv(f'scripts_upto_TEST.csv')


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

