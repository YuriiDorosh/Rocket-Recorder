import platform
import pyscreenshot as ImageGrab
from tkinter.filedialog import asksaveasfilename
import pyautogui


def make_screenshot():
    """
    Capture a screenshot of the screen.
    """
    if platform.system() == "Linux":
        screenshot = ImageGrab.grab()
        save_path = asksaveasfilename()
        screenshot.save(save_path + "_screenshot.png")
    else:
        my_screenshot = pyautogui.screenshot()
        save_path = asksaveasfilename()
        my_screenshot.save(save_path + "_screenshot.png")
