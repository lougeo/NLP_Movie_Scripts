# Louis George
# API scraper for:
# imdb.com as of Feb 2020

import numpy as np 
import pandas as pd 

from selenium import webdriver

class IMDbScraper():

    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\louis\Downloads\Chromedriver\chromedriver_win32\chromedriver.exe")

    def get_info(self):

        self.movie_info = []
        self.movie_id_dyn = []

        self.df = pd.read_csv('imbd_ids.csv').drop('Unnamed: 0', axis=1)

        for i in self.df['ID']:

            self.movie_id_dyn.append(i)

            try:
                self.driver.get(f'https://www.imdb.com/title/{i}/')

                info = self.driver.find_element_by_xpath('//*[@id="titleDetails"]')
                self.movie_info.append(info.text)
            except:
                self.movie_info.append(np.nan)

        df_out = pd.DataFrame({'ID':self.movie_id_dyn,
                               'info':self.movie_info})
        df_out.to_csv('../../data/imdb_scrape.csv')