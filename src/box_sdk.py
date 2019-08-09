from boxsdk import JWTAuth
from boxsdk import Client

from src import *


box_client = Client(JWTAuth.from_settings_file(BOX_CONFIG_FILE_PATH))
