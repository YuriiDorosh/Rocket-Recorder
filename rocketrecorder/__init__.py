import os

from .open_folder import open_the_folder
from .rocket_recorder import RocketRecorder
from .screen_recorder import record_windows, record_linux

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "static", "img")
