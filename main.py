# DDR A: .mw-parser-output > ul a:nth-child(1)
# DDR Supernova: .mw-parser-output > ul a:nth-child(1)

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

if __name__ == "__main__":

    supernova_url = 'https://remywiki.com/DanceDanceRevolution_SuperNOVA_Full_Song_List#DanceDanceRevolution_Solo_Series_.288_Songs.29'

    r = requests.get(supernova_url).content
    soup = BeautifulSoup(r)
    songs = soup.select('.mw-parser-output > ul a:nth-child(1)')
    songs = [song.contents[0] for song in songs]

    x = 4