from tqdm import tqdm

from src import *
from src import azlyrics


def scrape():
    for artist_letter in tqdm(AZ_LYRICS_ARTIST_LETTER_LIST, total=len(AZ_LYRICS_ARTIST_LETTER_LIST)):
        artist_url_list = azlyrics.get_artist_url_list(artist_letter)
        for artist_name, artist_url in tqdm(artist_url_list, total=len(artist_url_list)):
            print(f'Continue implementation with {artist_name} / {artist_url}')


if __name__ == '__main__':
    scrape()
