from tqdm import tqdm

from src import *
from src import azlyrics, csv_parser


def scrape():
    for artist_letter in tqdm(AZ_LYRICS_ARTIST_LETTER_LIST, total=len(AZ_LYRICS_ARTIST_LETTER_LIST)):
        artist_url_list = azlyrics.get_artist_url_list(artist_letter)
        for artist_name, artist_url in tqdm(artist_url_list, total=len(artist_url_list)):
            song_url_list = azlyrics.get_song_url_list(artist_url)
            for song_name, song_url in tqdm(song_url_list, total=len(song_url_list)):
                if not csv_parser.exists_song(artist_letter, artist_url, song_url):
                    song_lyrics = azlyrics.get_song_lyrics(song_url)
                    csv_parser.append_to_csv(artist_name, artist_url, song_name, song_url, song_lyrics, artist_letter)


if __name__ == '__main__':
    scrape()
