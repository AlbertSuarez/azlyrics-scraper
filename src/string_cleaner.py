import re
import unidecode

from src import *


def clean_url(url_str):
    url_str = url_str.lower()
    url_str = url_str.strip()
    return url_str


def clean_name(name_str):
    name_str = name_str.lower()
    name_str = name_str.strip()
    name_str = unidecode.unidecode(name_str)
    return name_str


def clean_lyrics(lyrics_str):
    lyrics_str = lyrics_str.lower()
    lyrics_str = lyrics_str.strip()
    lyrics_str = unidecode.unidecode(lyrics_str)
    lyrics_str = re.sub('[(\[].*?[)\]]', '', lyrics_str)
    for _ in range(0, STR_CLEAN_TIMES):
        for to_be_replaced, to_replace in STR_CLEAN_DICT.items():
            lyrics_str = lyrics_str.replace(to_be_replaced, to_replace)
    lyrics_str = lyrics_str.strip()
    return lyrics_str
