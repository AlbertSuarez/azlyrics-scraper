AZ_LYRICS_BASE_URL = 'https://www.azlyrics.com'
ARTIST_LETTER_LIST = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '19'
]

BASE = 'Mozilla/5.0'
USER_AGENT_LIST = [
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
RETRIES_AMOUNT = 3
SLEEP_TIME_BETWEEN_RETRIES = 0.5


__all__ = [
    'AZ_LYRICS_BASE_URL',
    'ARTIST_LETTER_LIST',
    'USER_AGENT_LIST',
    'RETRIES_AMOUNT',
    'SLEEP_TIME_BETWEEN_RETRIES'
]
