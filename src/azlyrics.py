import time
import random
import requests

from bs4 import BeautifulSoup

from src import *
from src import string_cleaner


def _get_html(url):
    time.sleep(random.uniform(SCRAPE_RTD_MINIMUM, SCRAPE_RTD_MAXIMUM))  # RTD
    for i in range(0, SCRAPE_RETRIES_AMOUNT):
        try:
            if SCRAPE_USER_AGENT_USE_RANDOM:
                headers = {'User-Agent': random.choice(SCRAPE_USER_AGENT_LIST)}
            else:
                headers = {'User-Agent': SCRAPE_USER_AGENT}
            response = requests.get(url, headers=headers)
            assert response.ok
            html_content = response.content
            return html_content
        except Exception as e:
            if i == SCRAPE_RETRIES_AMOUNT - 1:
                print(f'Unable to retrieve HTML from {url}: {e}')
            else:
                time.sleep(SCRAPE_SLEEP_TIME_BETWEEN_RETRIES)
    return None


def get_artist_url_list(artist_letter):
    artist_url_list = []

    try:
        artist_letter_url = f'{AZ_LYRICS_BASE_URL}/{artist_letter}.html'
        html_content = _get_html(artist_letter_url)
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')

            column_list = soup.find_all('div', {'class': 'artist-col'})
            for column in column_list:
                for a in column.find_all('a'):
                    artist_name = string_cleaner.clean_name(a.text)
                    artist_url = string_cleaner.clean_url('{}/{}'.format(AZ_LYRICS_BASE_URL, a['href']))
                    artist_url_list.append((artist_name, artist_url))
    except Exception as e:
        print(f'Error while getting artists from letter {artist_letter}: {e}')

    return artist_url_list


def get_song_url_list(artist_url):
    song_url_list = []

    try:
        html_content = _get_html(artist_url)
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')

            list_album_div = soup.find('div', {'id': 'listAlbum'})
            for a in list_album_div.find_all('a'):
                song_name = string_cleaner.clean_name(a.text)
                artist_url = string_cleaner.clean_url('{}/{}'.format(AZ_LYRICS_BASE_URL, a['href'].replace('../', '')))
                song_url_list.append((song_name, artist_url))
    except Exception as e:
        print(f'Error while getting songs from artist {artist_url}: {e}')

    return song_url_list


def get_song_lyrics(song_url):
    song_lyrics = ''

    try:
        html_content = _get_html(song_url)
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            div_list = [div.text for div in soup.find_all('div', {'class': None})]
            song_lyrics = max(div_list, key=len)
            song_lyrics = string_cleaner.clean_lyrics(song_lyrics)
    except Exception as e:
        print(f'Error while getting lyrics from song {song_url}: {e}')

    return song_lyrics
