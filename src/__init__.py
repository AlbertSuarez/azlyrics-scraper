# AZLyrics website
AZ_LYRICS_BASE_URL = 'https://www.azlyrics.com'
AZ_LYRICS_ARTIST_LETTER_LIST = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '19'
]

# Scrapping
BASE = 'Mozilla/5.0'
SCRAPE_RTD_MINIMUM = 4
SCRAPE_RTD_MAXIMUM = 6
SCRAPE_USER_AGENT_USE_RANDOM = False
SCRAPE_USER_AGENT = f'{BASE} (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) ' \
    f'Chrome/75.0.3770.100 Safari/537.36'
SCRAPE_USER_AGENT_LIST = [
    f'{BASE} (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    f'{BASE} (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    f'{BASE} (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    f'{BASE} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    f'{BASE} (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    f'{BASE} (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0',
    f'{BASE} (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
    f'{BASE} (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    f'{BASE} (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
]
SCRAPE_RETRIES_AMOUNT = 3
SCRAPE_SLEEP_TIME_BETWEEN_RETRIES = 10

# CSV
CSV_FILE = 'data/azlyrics_lyrics'
CSV_HEADER_ARTIST_NAME = 'ARTIST_NAME'
CSV_HEADER_ARTIST_URL = 'ARTIST_URL'
CSV_HEADER_SONG_NAME = 'SONG_NAME'
CSV_HEADER_SONG_URL = 'SONG_URL'
CSV_HEADER_LYRICS = 'LYRICS'

# String cleaning
STR_CLEAN_TIMES = 3
STR_CLEAN_DICT = {
    '\n\n': '\n',
    '\n\r\n': '\n',
    '\r': '',
    '\n': ', ',
    '  ': ' ',
    ' ,': ',',
    ' .': '.',
    ' :': ':',
    ' !': '!',
    ' ?': '?',
    ',,': ',',
    '..': '.',
    '::': ':',
    '!!': '!',
    '??': '?',
    '.,': '.',
    '.:': '.',
    ',.': ',',
    ',:': ',',
    ':,': ':',
    ':.': ':'
}

# Box integration
BOX_CONFIG_FILE_PATH = 'data/jwt_config.json'
BOX_RETRIES = 3
BOX_RTM = 3
BOX_FOLDER_ROOT_ID = '0'
BOX_FOLDER_APP_ID = '84132126414'
BOX_LINK_OPEN_ACCESS = 'open'
BOX_LINK_ALLOW_DOWNLOAD = True
BOX_LINK_ALLOW_PREVIEW = True


__all__ = [
    'AZ_LYRICS_BASE_URL',
    'AZ_LYRICS_ARTIST_LETTER_LIST',
    'SCRAPE_RTD_MINIMUM',
    'SCRAPE_RTD_MAXIMUM',
    'SCRAPE_USER_AGENT_USE_RANDOM',
    'SCRAPE_USER_AGENT',
    'SCRAPE_USER_AGENT_LIST',
    'SCRAPE_RETRIES_AMOUNT',
    'SCRAPE_SLEEP_TIME_BETWEEN_RETRIES',
    'CSV_FILE',
    'CSV_HEADER_ARTIST_NAME',
    'CSV_HEADER_ARTIST_URL',
    'CSV_HEADER_SONG_NAME',
    'CSV_HEADER_SONG_URL',
    'CSV_HEADER_LYRICS',
    'STR_CLEAN_TIMES',
    'STR_CLEAN_DICT',
    'BOX_CONFIG_FILE_PATH',
    'BOX_RETRIES',
    'BOX_RTM',
    'BOX_FOLDER_ROOT_ID',
    'BOX_FOLDER_APP_ID',
    'BOX_LINK_OPEN_ACCESS',
    'BOX_LINK_ALLOW_DOWNLOAD',
    'BOX_LINK_ALLOW_PREVIEW'
]
