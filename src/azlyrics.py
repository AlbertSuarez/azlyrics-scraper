import random
import time

import requests

from bs4 import BeautifulSoup

from src import *


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

    artist_letter_url = f'{AZ_LYRICS_BASE_URL}/{artist_letter}.html'
    html_content = _get_html(artist_letter_url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')

        column_list = soup.find_all('div', {'class': 'artist-col'})
        for column in column_list:
            for a in column.find_all('a'):
                artist_name = a.text
                artist_url = '{}/{}'.format(AZ_LYRICS_BASE_URL, a['href'])
                artist_url_list.append((artist_name, artist_url))

    return artist_url_list
