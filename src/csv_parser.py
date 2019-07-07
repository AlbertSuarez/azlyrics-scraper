import os
import csv

from src import *


def exists_song(csv_letter, artist_url, song_url):
    csv_file_name = f'{CSV_FILE}_{csv_letter}.csv'
    exists_file = os.path.isfile(csv_file_name)
    if exists_file:
        with open(csv_file_name, 'r') as file:
            rows = [row for row in csv.reader(file)][1:]
            rows = [row for row in rows if row[1] == artist_url and row[3] == song_url]
            if rows:
                return True
    return False


def append_to_csv(artist_name, artist_url, song_name, song_url, song_lyrics, csv_letter):
    if song_lyrics:
        csv_file_name = f'{CSV_FILE}_{csv_letter}.csv'
        exists_file = os.path.isfile(csv_file_name)
        with open(csv_file_name, 'a') as file:
            if not exists_file:
                file.write(
                    f'"{CSV_HEADER_ARTIST_NAME}","{CSV_HEADER_ARTIST_URL}",'
                    f'"{CSV_HEADER_SONG_NAME}","{CSV_HEADER_SONG_URL}","{CSV_HEADER_LYRICS}"'
                )
            file.write(f'\n"{artist_name}","{artist_url}","{song_name}","{song_url}","{song_lyrics}"')
