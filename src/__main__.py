import os

from src import *
from src import azlyrics, csv_parser, box_sdk


def scrape():
    """
    Processes the main function of the scraper.
    :return: All AZLyrics scraped.
    """
    for artist_letter in AZ_LYRICS_ARTIST_LETTER_LIST:
        # Logging stuff
        print(f'[1] Processing [{artist_letter}] letter...')

        # Downloads file if it is available on Box folder.
        csv_file_name = f'{CSV_FILE}_{artist_letter}.csv'
        print(f'[1] Searching for {csv_file_name} in Box folder...')
        file_id = box_sdk.search_file(BOX_FOLDER_APP_ID, csv_file_name.split('/')[-1])
        if file_id:
            print(f'[1] ---> File found with id [{file_id}]!')
            box_sdk.download_file(file_id, csv_file_name)

        # Iterates over all artists with the given letter.
        print('[1] Scraping artists URLs...')
        artist_url_list = azlyrics.get_artist_url_list(artist_letter)
        print(f'[1] ---> {len(artist_url_list)} artists found with letter [{artist_letter}]')
        for artist_name, artist_url in artist_url_list:
            some_song_added = False
            print(f'[2] Scraping song URLs for {artist_name}...')
            song_url_list = azlyrics.get_song_url_list(artist_url)
            print(f'[2] ---> {len(artist_url_list)} artists found with letter [{artist_letter}]')
            for song_name, song_url in song_url_list:
                print(f'[3] Scraping lyrics for song: [{song_name}]')
                if not csv_parser.exists_song(artist_letter, artist_url, song_url):
                    song_lyrics = azlyrics.get_song_lyrics(song_url)
                    csv_parser.append_to_csv(artist_name, artist_url, song_name, song_url, song_lyrics, artist_letter)
                    some_song_added = True
            # Uploads or updates the CSV on Box per every artist.
            if some_song_added:
                if file_id:
                    file_id = box_sdk.update_file(file_id, csv_file_name)
                else:
                    file_id = box_sdk.upload_file(BOX_FOLDER_APP_ID, csv_file_name)

        # Removes the local version of the CSV for saving storage.
        if os.path.isfile(csv_file_name):
            os.remove(csv_file_name)


if __name__ == '__main__':
    iteration = 1
    while True:
        print(f'Starting iteration number {iteration}...')
        scrape()
        iteration += 1

