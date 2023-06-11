from tkinter import *
import os
import platform
import datetime
import subprocess
import threading
import pyscreenshot as ImageGrab
from tkinter.filedialog import *
from tkinter import messagebox
from rocketrecorder.open_folder import open_folder
from rocketrecorder.screen_recorder import record_windows, record_linux
import pyautogui

class RocketRecorder:
    def __init__(self):
        """
        Initialize the RocketRecorder application.
        """
        self.root = Tk()
        self.root.geometry("1200x600")
        self.root.title("rocket recorder")
        self.root.config(bg="#F8F8FF")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.resizable(False, False)

        self.img = PhotoImage(file="rocketrecorder/photo/space.png")
        self.bg = PhotoImage(file="rocketrecorder/for_new_window/wininfo.png")
        self.start_btn_image = PhotoImage(file="rocketrecorder/buttons/start.png")
        self.stop_btn_image = PhotoImage(file="rocketrecorder/buttons/stop.png")
        self.folder_btn_image = PhotoImage(file="rocketrecorder/buttons/folder.png")
        self.tip_btn_image = PhotoImage(file="rocketrecorder/buttons/tip.png")
        self.scr_btn_image = PhotoImage(file="rocketrecorder/buttons/screen1.png")

        self.app_label = Label(
            self.root,
            text="Rocket recorder",
            image=self.img,
            bg="#A9A9A9",
            font=("rockwell", 26, "bold"),
            padx=500,
            pady=32,
        )
        self.app_label.grid(columnspan=3)

        self.create_buttons()

    def create_buttons(self):
        """
        Create the buttons in the application.
        """
        record_btn = Button(
            self.root,
            command=self.start_recording,
            image=self.start_btn_image,
            bg="#F8F8FF",
            activebackground="#F8F8FF",
            bd=0,
        )
        record_btn.grid(row=5, column=0, pady=100)

        stop_btn = Button(
            self.root,
            command=self.stop_recording,
            image=self.stop_btn_image,
            bg="#F8F8FF",
            activebackground="#F8F8FF",
            bd=0,
        )
        stop_btn.grid(row=5, column=1, pady=3)

        folder_btn = Button(
            self.root,
            command=self.open_folder,
            image=self.folder_btn_image,
            bg="#F8F8FF",
            activebackground="#F8F8FF",
            bd=0,
        )
        folder_btn.grid(row=5, column=2, pady=3)

        tip_btn = Button(
            self.root,
            command=self.start_window,
            image=self.tip_btn_image,
            bg="#A9A9A9",
            bd=2,
        )
        tip_btn.place(x=1148, y=20)

        scr_btn = Button(
            self.root,
            command=self.make_screenshot,
            image=self.scr_btn_image,
            bg="#A9A9A9",
            bd=2,
        )
        scr_btn.place(x=50, y=60)

    def start_window(self):
        """
        Open the "Tips" window.
        """
        new_window = Toplevel(self.root)
        new_window.geometry("400x300")
        new_window.title("Tips")
        if platform.system() == "Windows":
            new_window.iconbitmap("rocketrecorder/for_new_window/icoo.ico")
        new_window.resizable(False, False)
        new_window.wm_attributes("-topmost", 1)
        label2 = Label(new_window, image=self.bg)
        label2.place(x=0, y=0)

    def start_recording(self):
        """
        Start the screen recording based on the platform.
        """
        if platform.system() == "Linux":
            threading.Thread(target=record_linux).start()
        else:
            threading.Thread(target=record_windows).start()

    def stop_recording(self):
        """
        Stop the screen recording based on the platform.
        """
        if platform.system() == "Linux":
            subprocess.run(["pkill", "ffmpeg"])
        else:
            stop_video_recording()
            free_resources()

    def make_screenshot(self):
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

    def open_folder(self):
        """
        Open the folder containing the recorded videos.
        """
        open_folder()

    def on_closing(self):
        """
        Handle the closing of the application window.
        """
        if messagebox.askokcancel(
                "Exit", "Do You want to exit the App?\n Data may be corrupted"
        ):
            self.root.destroy()

    def run(self):
        """
        Run the RocketRecorder application.
        """
        self.root.mainloop()


if __name__ == "__main__":
    app = RocketRecorder()
    app.run()
