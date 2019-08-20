import time
import random
import requests

from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent

from src import *
from src import string_cleaner


def _get_html(url):
    """
    Retrieves the HTML content given a Internet accessible URL.
    :param url: URL to retrieve.
    :return: HTML content formatted as String, None if there was an error.
    """
    time.sleep(random.uniform(SCRAPE_RTD_MINIMUM, SCRAPE_RTD_MAXIMUM))  # RTD
    for i in range(0, SCRAPE_RETRIES_AMOUNT):
        try:
            with Controller.from_port(port=9051) as c:
                c.authenticate()
                c.signal(Signal.NEWNYM)
            proxies = {'http': SCRAPE_PROXY, 'https': SCRAPE_PROXY}
            headers = {'User-Agent': UserAgent().random}
            response = requests.get(url, proxies=proxies, headers=headers)
            assert response.ok
            html_content = response.content
            return html_content
        except Exception as e:
            if i == SCRAPE_RETRIES_AMOUNT - 1:
                print(f'Unable to retrieve HTML from {url}: {e}')
            else:
                time.sleep(random.uniform(SCRAPE_RTD_ERROR_MINIMUM, SCRAPE_RTD_ERROR_MAXIMUM))
    return None


def get_artist_url_list(artist_letter):
    """
    Retrieves the AZLyrics website URLs for all the artists given its first character.
    :param artist_letter: First character of an artist.
    :return: List of pairs containing the artist name and its AZLyrics URL.
    """
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
    """
    Retrieves the AZLyrics website URLs for all the songs from an artist AZLyrics URL.
    :param artist_url: AZLyrics URL from a given artist.
    :return: List of pairs containing the song name and its AZLyrics URL.
    """
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
    """
    Retrieves and cleans the lyrics of a song given its AZLyrics URL.
    :param song_url: AZLyrics URL from a given song.
    :return: Cleaned and formatted song lyrics.
    """
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
