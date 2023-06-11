# from tkinter import *
# import os
# import platform
# import datetime
# import subprocess
# import threading
# import pyscreenshot as ImageGrab
# from tkinter.filedialog import *
# from tkinter import messagebox
# from screen_recorder_sdk import screen_recorder
# import pyautogui
#
#
# # Reasking if User want to leave the app
# def on_closing():
#     if messagebox.askokcancel("Exit", "Do You want to exit the App?\n Data may be corrupted"):
#         root.destroy()
#
#
# # Function to start recording on Linux
# def record_linux():
#     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     file_name = f"video_{timestamp}.mp4"
#
#     subprocess.run([
#         "ffmpeg",
#         "-video_size", "1920x1080",
#         "-framerate", "30",
#         "-f", "x11grab",
#         "-i", ":0.0",
#         file_name
#     ])
#
#
# # Function to start recording
# def start_recording():
#     if platform.system() == "Linux":
#         threading.Thread(target=record_linux).start()
#     else:
#         screen_recorder.enable_dev_log()
#         params = screen_recorder.RecorderParams()
#         screen_recorder.init_resources(params)
#         timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#         file_name = f"video_{timestamp}.mp4"
#         screen_recorder.start_video_recording(os.path.join(f"{file_name}"), 30, 8000000, True)
#
#
# # Function to stop recording
# def stop_recording():
#     if platform.system() == "Linux":
#         subprocess.run(["pkill", "ffmpeg"])
#     else:
#         screen_recorder.stop_video_recording()
#         screen_recorder.free_resources()
#
#
# # Function to open the folder
# def open_folder():
#     if platform.system() == "Linux":
#         subprocess.run(["xdg-open", os.getcwd()])
#     else:
#         path = os.path.realpath(os.getcwd())
#         os.startfile(path)
#
#
# # Function to capture a screenshot
# def make_screenshot():
#     if platform.system() == "Linux":
#         screenshot = ImageGrab.grab()
#         save_path = asksaveasfilename()
#         screenshot.save(save_path + "_screenshot.png")
#     else:
#         myscreenshot = pyautogui.screenshot()
#         save_path = asksaveasfilename()
#         myscreenshot.save(save_path + "_screenshot.png")
#
#
# # Function to open the tips window
# def start_window_1():
#     new_window_1 = Toplevel(root)
#     new_window_1.geometry("400x300")
#     new_window_1.title("Tips")
#     new_window_1.resizable(False, False)
#     new_window_1.wm_attributes("-topmost", 1)
#     label2 = Label(new_window_1, image=bg)
#     label2.place(x=0, y=0)
#
#
# # head
# root = Tk()
# root.geometry("1200x600")
# root.title("rocket recorder")
# root.config(bg="#F8F8FF")
# root.protocol("WM_DELETE_WINDOW", on_closing)
# root.resizable(False, False)
#
# img = PhotoImage(file="photo//space.png")
#
# app_label = Label(
#     root,
#     text="Rocket recorder",
#     image=img,
#     bg="#A9A9A9",
#     font=("rockwell", 26, "bold"),
#     padx=500,
#     pady=32,
# )
# app_label.grid(columnspan=3)
# bg = PhotoImage(file="for_new_window//wininfo.png")
#
# # Buttons
# photo = PhotoImage(file=os.path.join("buttons//start.png"))
# record_btn = Button(
#     root,
#     command=start_recording,
#     image=photo,
#     bg="#F8F8FF",
#     activebackground="#F8F8FF",
#     bd=0,
# )
# record_btn.grid(row=5, column=0, pady=100)
#
# photo2 = PhotoImage(file=os.path.join("buttons//stop.png"))
# stop_btn = Button(
#     root,
#     command=stop_recording,
#     image=photo2,
#     bg="#F8F8FF",
#     activebackground="#F8F8FF",
#     bd=0,
# )
# stop_btn.grid(row=5, column=1, pady=3)
#
# photo3 = PhotoImage(file=os.path.join("buttons//folder.png"))
# folder_btn = Button(
#     root,
#     command=open_folder,
#     image=photo3,
#     bg="#F8F8FF",
#     activebackground="#F8F8FF",
#     bd=0,
# )
# folder_btn.grid(row=5, column=2, pady=3)
#
# photo4 = PhotoImage(file=os.path.join("buttons//tip.png"))
# tip_btn = Button(root, command=start_window_1, image=photo4, bg="#A9A9A9", bd=2).place(
#     x=1148, y=20
# )
#
# photo5 = PhotoImage(file=os.path.join("buttons//screen1.png"))
# scr_btn = Button(root, command=make_screenshot, image=photo5, bg="#A9A9A9", bd=2).place(
#     x=50, y=60
# )
#
# root.mainloop()


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

class RocketRecorder:
    def __init__(self):
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

        tip_btn = Button(self.root, command=self.start_window_1, image=self.tip_btn_image, bg="#A9A9A9", bd=2)
        tip_btn.place(x=1148, y=20)

        scr_btn = Button(self.root, command=self.make_screenshot, image=self.scr_btn_image, bg="#A9A9A9", bd=2)
        scr_btn.place(x=50, y=60)

    def start_window_1(self):
        new_window_1 = Toplevel(self.root)
        new_window_1.geometry("400x300")
        new_window_1.title("Tips")
        new_window_1.resizable(False, False)
        new_window_1.wm_attributes("-topmost", 1)
        label2 = Label(new_window_1, image=self.bg)
        label2.place(x=0, y=0)

    def start_recording(self):
        if platform.system() == "Linux":
            threading.Thread(target=self.record_linux).start()
        else:
            screen_recorder.enable_dev_log()
            params = screen_recorder.RecorderParams()
            screen_recorder.init_resources(params)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"video_{timestamp}.mp4"
            screen_recorder.start_video_recording(os.path.join(f"{file_name}"), 30, 8000000, True)

    def record_linux(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"video_{timestamp}.mp4"

        subprocess.run([
            "ffmpeg",
            "-video_size", "1920x1080",
            "-framerate", "30",
            "-f", "x11grab",
            "-i", ":0.0",
            file_name
        ])

    def stop_recording(self):
        if platform.system() == "Linux":
            subprocess.run(["pkill", "ffmpeg"])
        else:
            screen_recorder.stop_video_recording()
            screen_recorder.free_resources()

    def open_folder(self):
        if platform.system() == "Linux":
            subprocess.run(["xdg-open", os.getcwd()])
        else:
            path = os.path.realpath(os.getcwd())
            os.startfile(path)

    def make_screenshot(self):
        if platform.system() == "Linux":
            screenshot = ImageGrab.grab()
            save_path = asksaveasfilename()
            screenshot.save(save_path + "_screenshot.png")
        else:
            myscreenshot = pyautogui.screenshot()
            save_path = asksaveasfilename()
            myscreenshot.save(save_path + "_screenshot.png")

    def on_closing(self):
        if messagebox.askokcancel(
                "Exit", "Do You want to exit the App?\n Data may be corrupted"
        ):
            self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RocketRecorder()
    app.run()


