import requests
from bs4 import BeautifulSoup


def get_songs_from_url(url):
    r = requests.get(url).content
    soup = BeautifulSoup(r, 'html.parser')
    song_info = soup.select('.mw-parser-output > ul a:nth-child(1)')
    song_names = {song.contents[0] for song in song_info}
    return song_names


if __name__ == "__main__":

    supernova_url = 'https://remywiki.com/DanceDanceRevolution_SuperNOVA_Full_Song_List'
    a_url = 'https://remywiki.com/DanceDanceRevolution_A_Full_Song_List'

    supernova_songs = get_songs_from_url(supernova_url)
    a_songs = get_songs_from_url(a_url)

    supernova_only = supernova_songs - a_songs

    # Discrepancy between supernova song listings and A song listings;
    # 99% of the songs with parenthesis are actually in DDR A, so remove them
    supernova_only = filter(lambda x: '(' not in x, supernova_only)

    # Sort alphabetically for easier finding in machine
    supernova_only = sorted(supernova_only, key=str.casefold)
    print("\n".join(supernova_only))
