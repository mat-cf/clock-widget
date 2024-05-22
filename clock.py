from tkinter import *
import tkinter.font as tkFont
import time
from time import strftime
import locale

locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')

root = Tk()

root.overrideredirect(1)
root.wm_attributes("-transparentcolor", "gray99")

def close(event):
    root.destroy()

root.bind('<Escape>', close)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

timeframe = Frame(root, width=screen_width, height=screen_height, bg="gray99")
timeframe.grid(row=0, column=0)

font_large = tkFont.Font(family="Segoe UI Variable", size=60)
font_small = tkFont.Font(family="Segoe UI Variable", size=25)

class TimeFrame:
    def __init__(self, parent):
        self.tkintertime = StringVar()
        self.timelabel = Label(parent, textvariable=self.tkintertime, fg="white", bg="gray99", font=font_large)
        self.timelabel.place(x=screen_width - 20, y=0, anchor="ne") 

        self.tkinterdate = StringVar()
        self.datelabel = Label(parent, textvariable=self.tkinterdate, fg="white", bg="gray99", font=font_small)  
        self.datelabel.place(x=screen_width - 20, y=80, anchor="ne") 

    def update_time(self):
        self.tkintertime.set(strftime("%H:%M"))
        day = strftime("%A")
        date = strftime("%d")
        month = strftime("%B")
        formatted_date = f"{day}, {date} de {month}"
        self.tkinterdate.set(formatted_date)
        root.after(1000, self.update_time) 

def on_drag_start(event):
    root._drag_data = {"x": event.x, "y": event.y}

def on_drag_motion(event):
    x = root.winfo_x() - root._drag_data["x"] + event.x
    y = root.winfo_y() - root._drag_data["y"] + event.y
    root.geometry(f"+{x}+{y}")

root.bind("<Button-1>", on_drag_start)
root.bind("<B1-Motion>", on_drag_motion)

time_frame_instance = TimeFrame(timeframe)

time_frame_instance.update_time()

root.mainloop()
