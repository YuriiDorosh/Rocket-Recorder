from tkinter import *
import os
from screen_recorder_sdk import screen_recorder
from tkinter import messagebox
import pyautogui
from tkinter.filedialog import *
import sounddevice as sound
from scipy.io.wavfile import write
import wavio as wv

# Reasking if User want to leave the app

def on_closing():
    if messagebox.askokcancel('Exit', 'Do You want to exit the App?\n Data may be corrupted'):
        root.destroy()

#head

root=Tk()
root.geometry('1200x600')
root.title('rocket recorder')
root.iconbitmap('rocketico.ico')
root.config(bg='#F8F8FF')
root.protocol('WM_DELETE_WINDOW', on_closing)
root.resizable(False,False)



img = PhotoImage(file='photo//space.png')

app_label = Label(root,text='Rocket recorder',
                  image=img,               
                  bg='#A9A9A9',
                  font=('rockwell',26,'bold'),
                  padx=500,pady=32
               
)
app_label.grid(columnspan=3)
bg = PhotoImage(file = 'for_new_window//wininfo.png')
#function

  #function for tips
def start_window_1():
    new_window_1 = Toplevel(root)
    new_window_1.geometry('400x300')
    new_window_1.title('Tips')
    new_window_1.iconbitmap('for_new_window//icoo.ico')
    new_window_1.resizable(False,False)
    new_window_1.wm_attributes('-topmost',1)
    label2 = Label(new_window_1,image=bg)
    label2.place(x = 0, y = 0)
    

         
  #function for start/recording
def start_recording():
    screen_recorder.enable_dev_log()
    params = screen_recorder.RecorderParams()
    screen_recorder.init_resources(params)
    screen_recorder.start_video_recording(os.path.join('video.mp4'),30,8000000,True)
    record_btn['state'] = 'disabled'
    stop_btn['state'] = 'normal'


  #function for stop
def stop_recording():
    screen_recorder.stop_video_recording()
    screen_recorder.free_resources()
    record_btn['state'] = 'normal'
    stop_btn['state'] = 'disabled'


  #function for folder mechanics
def open_folder():
    path = os.path.realpath(os.getcwd())
    os.startfile(path)


  #function for screenshot
def make_screenshot():
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+'_screenshot.png')

    

#buttons

  #start

photo = PhotoImage(file=os.path.join('buttons//start.png'))
record_btn = Button(root,
                    command=start_recording,
                    image=photo,
                    bg='#F8F8FF',
                    activebackground='#F8F8FF',
                    bd=0
)
record_btn.grid(row=5,
                column=0,
                pady=100
)

  #stop

photo2 = PhotoImage(file=os.path.join('buttons//stop.png'))
stop_btn = Button(root,
                  command=stop_recording,
                  image=photo2,
                  bg='#F8F8FF',
                  activebackground='#F8F8FF',
                  bd=0
)
stop_btn.grid(row=5,
              column=1,
              pady=3
)

  #folder

photo3 = PhotoImage(file=os.path.join('buttons//folder.png'))
folder_btn = Button(root,
                    command= open_folder,
                    image=photo3,
                    bg='#F8F8FF',
                    activebackground='#F8F8FF',
                    bd=0
)
folder_btn.grid(row=5,
                column=2,
                pady=3
)

  #tip

photo4 = PhotoImage(file=os.path.join('buttons//tip.png'))
tip_btn = Button(root,
                 command=start_window_1,
                 image=photo4,
                 bg='#A9A9A9',
                 bd=2       
).place(x = 1148, y = 20)
                    
  #screenshot

photo5 = PhotoImage(file=os.path.join('buttons//screen1.png'))
scr_btn = Button(root,
                 command=make_screenshot,
                 image=photo5,
                 bg='#A9A9A9',
                 bd=2
).place(x=50,y=60)


            

stop_btn['state'] = 'disabled'
root.mainloop()