import os
import platform
import subprocess

def open_folder():
    """
    Open the folder containing the recorded videos.
    """
    if platform.system() == "Linux":
        subprocess.run(["xdg-open", os.getcwd()])
    else:
        path = os.path.realpath(os.getcwd())
        os.startfile(path)
