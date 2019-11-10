# AZLyrics website
AZ_LYRICS_BASE_URL = 'https://www.azlyrics.com'
AZ_LYRICS_ARTIST_LETTER_LIST = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '19'
]

# Scrapping
SCRAPE_PROXY = 'socks5://127.0.0.1:9050'
SCRAPE_RTD_MINIMUM = 0.1
SCRAPE_RTD_MAXIMUM = 0.5
SCRAPE_RETRIES_AMOUNT = 10
SCRAPE_RTD_ERROR_MINIMUM = 0.5
SCRAPE_RTD_ERROR_MAXIMUM = 1

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
    'SCRAPE_PROXY',
    'SCRAPE_RTD_MINIMUM',
    'SCRAPE_RTD_MAXIMUM',
    'SCRAPE_RETRIES_AMOUNT',
    'SCRAPE_RTD_ERROR_MINIMUM',
    'SCRAPE_RTD_ERROR_MAXIMUM',
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
