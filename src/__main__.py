import os

from tqdm import tqdm

from src import *
from src import azlyrics, csv_parser, box_sdk


def scrape():
    for artist_letter in tqdm(AZ_LYRICS_ARTIST_LETTER_LIST, total=len(AZ_LYRICS_ARTIST_LETTER_LIST)):
        # Downloads file if it is available on Box folder.
        csv_file_name = f'{CSV_FILE}_{artist_letter}.csv'
        file_id = box_sdk.search_file(BOX_FOLDER_APP_ID, csv_file_name.split('/')[-1])
        if file_id:
            box_sdk.download_file(file_id, csv_file_name)

        # Iterates over all artists with the given letter.
        artist_url_list = azlyrics.get_artist_url_list(artist_letter)
        for artist_name, artist_url in tqdm(artist_url_list, total=len(artist_url_list)):
            song_url_list = azlyrics.get_song_url_list(artist_url)
            for song_name, song_url in tqdm(song_url_list, total=len(song_url_list)):
                if not csv_parser.exists_song(artist_letter, artist_url, song_url):
                    song_lyrics = azlyrics.get_song_lyrics(song_url)
                    csv_parser.append_to_csv(artist_name, artist_url, song_name, song_url, song_lyrics, artist_letter)
            # Uploads or updates the CSV on Box per every artist.
            if file_id:
                file_id = box_sdk.update_file(file_id, csv_file_name)
            else:
                file_id = box_sdk.upload_file(BOX_FOLDER_APP_ID, csv_file_name)

        # Removes the local version of the CSV for saving storage.
        os.remove(csv_file_name)


if __name__ == '__main__':
    scrape()
