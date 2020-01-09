# DDR A: .mw-parser-output > ul a:nth-child(1)
# DDR Supernova: .mw-parser-output > ul a:nth-child(1)

import requests
from bs4 import BeautifulSoup

def get_songs_from_url(url):
    r = requests.get(url).content
    soup = BeautifulSoup(r)
    song_info = soup.select('.mw-parser-output > ul a:nth-child(1)')
    song_names = {song.contents[0] for song in song_info}
    return song_names

if __name__ == "__main__":

    supernova_url = 'https://remywiki.com/DanceDanceRevolution_SuperNOVA_Full_Song_List'
    a_url = 'https://remywiki.com/DanceDanceRevolution_A_Full_Song_List'

    supernova_songs = get_songs_from_url(supernova_url)
    a_songs = get_songs_from_url(a_url)

    print("\n".join(supernova_songs - a_songs))