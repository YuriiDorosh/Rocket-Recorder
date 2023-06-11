from tkinter import *
import os
import platform
import datetime
import subprocess
import threading
import pyscreenshot as ImageGrab
from tkinter.filedialog import *
from tkinter import messagebox
from screen_recorder_sdk import screen_recorder
import pyautogui


def open_folder():
    """
    Open the folder containing the recorded videos.
    """
    if platform.system() == "Linux":
        subprocess.run(["xdg-open", os.getcwd()])
    else:
        path = os.path.realpath(os.getcwd())
        os.startfile(path)


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

        self.img = PhotoImage(file="photo//space.png")
        self.bg = PhotoImage(file="for_new_window//wininfo.png")
        self.start_btn_image = PhotoImage(file=os.path.join("buttons//start.png"))
        self.stop_btn_image = PhotoImage(file=os.path.join("buttons//stop.png"))
        self.folder_btn_image = PhotoImage(file=os.path.join("buttons//folder.png"))
        self.tip_btn_image = PhotoImage(file=os.path.join("buttons//tip.png"))
        self.scr_btn_image = PhotoImage(file=os.path.join("buttons//screen1.png"))

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
            command=open_folder,
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
            new_window.iconbitmap("for_new_window//icoo.ico")
        new_window.resizable(False, False)
        new_window.wm_attributes("-topmost", 1)
        label2 = Label(new_window, image=self.bg)
        label2.place(x=0, y=0)

    @staticmethod
    def record_windows():
        """
        Record the screen using the screen_recorder_sdk on Windows.
        """
        screen_recorder.enable_dev_log()
        params = screen_recorder.RecorderParams()
        screen_recorder.init_resources(params)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"video_{timestamp}.mp4"
        screen_recorder.start_video_recording(
            os.path.join(f"{file_name}"), 30, 8000000, True
        )

    @staticmethod
    def record_linux():
        """
        Record the screen using ffmpeg on Linux.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"video_{timestamp}.mp4"

        subprocess.run(
            [
                "ffmpeg",
                "-video_size",
                "1920x1080",
                "-framerate",
                "30",
                "-f",
                "x11grab",
                "-i",
                ":0.0",
                file_name,
            ]
        )

    def start_recording(self):
        """
        Start the screen recording based on the platform.
        """
        if platform.system() == "Linux":
            threading.Thread(target=self.record_linux).start()
        else:
            threading.Thread(target=self.record_windows).start()

    @staticmethod
    def stop_recording():
        """
        Stop the screen recording based on the platform.
        """
        if platform.system() == "Linux":
            subprocess.run(["pkill", "ffmpeg"])
        else:
            screen_recorder.stop_video_recording()
            screen_recorder.free_resources()

    @staticmethod
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


