from boxsdk import JWTAuth
from boxsdk import Client

from src import *


def create_folder(folder_name):
    box_client = Client(JWTAuth.from_settings_file(BOX_CONFIG_FILE_PATH))
    for i in range(0, BOX_RETRIES):
        try:
            sub_folder = box_client.folder(BOX_FOLDER_ROOT_ID).create_subfolder(folder_name)
            return sub_folder.id
        except Exception as e:
            if i == BOX_RETRIES - 1:
                print(f'Error calling Box API creating the folder [{folder_name}] into folder root: {e}')
    return None


def create_shared_link(folder_id):
    box_client = Client(JWTAuth.from_settings_file(BOX_CONFIG_FILE_PATH))
    for i in range(0, BOX_RETRIES):
        try:
            shared_link = box_client.folder(folder_id).get_shared_link(
                access=BOX_LINK_OPEN_ACCESS,
                allow_download=BOX_LINK_ALLOW_DOWNLOAD,
                allow_preview=BOX_LINK_ALLOW_PREVIEW
            )
            return shared_link
        except Exception as e:
            if i == BOX_RETRIES - 1:
                print(f'Error calling Box API creating a shared link for folder [{folder_id}]: {e}')
    return None


def search_file(folder_id, file_name):
    box_client = Client(JWTAuth.from_settings_file(BOX_CONFIG_FILE_PATH))
    for i in range(0, BOX_RETRIES):
        try:
            for result in box_client.folder(folder_id).get_items():
                if result.name == file_name:
                    return result.id
            return None
        except Exception as e:
            if i == BOX_RETRIES - 1:
                print(f'Error calling Box API searching files into folder [{folder_id}] with name [{file_name}]: {e}')
    return None


def upload_file(folder_id, file_path):
    box_client = Client(JWTAuth.from_settings_file(BOX_CONFIG_FILE_PATH))
    for i in range(0, BOX_RETRIES):
        try:
            file_name = file_path.split('/')[-1]
            return box_client.folder(folder_id).upload(file_path, file_name)
        except Exception as e:
            if i == BOX_RETRIES - 1:
                print(f'Error calling Box API uploading the file [{file_path}] to folder with id [{folder_id}]: {e}')
    return None


def update_file(file_id, file_path):
    box_client = Client(JWTAuth.from_settings_file(BOX_CONFIG_FILE_PATH))
    for i in range(0, BOX_RETRIES):
        try:
            return box_client.file(file_id).update_contents(file_path)
        except Exception as e:
            if i == BOX_RETRIES - 1:
                print(f'Error calling Box API updating the file [{file_id}] with file [{file_path}]: {e}')
    return None


def download_file(file_id, file_path):
    box_client = Client(JWTAuth.from_settings_file(BOX_CONFIG_FILE_PATH))
    for i in range(0, BOX_RETRIES):
        try:
            with open(file_path, 'wb') as file:
                box_client.file(file_id).download_to(file)
            return True
        except Exception as e:
            if i == BOX_RETRIES - 1:
                print(f'Error calling Box API downloading the file [{file_id}] to file [{file_path}]: {e}')
    return None
