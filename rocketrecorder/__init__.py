import os

from .open_folder import open_the_folder
from .rocket_recorder import RocketRecorder
from .windows_screen_recorder import record
from .linux_screen_recorder import record

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "static", "img")
