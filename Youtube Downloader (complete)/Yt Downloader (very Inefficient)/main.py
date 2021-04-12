from pytube import YouTube
from tkinter import *


def radiobutton_clicked(value):
    global resolution
    resolution = value

def downloadButton(reso):
    url=url_entry.get()
    YouTube(url).streams.filter(res=f"{reso}", ).first().download()

root = Tk()
root.title("YTD")
root.geometry("500x200")
root.iconbitmap("yt.ico")
root.resizable(False, False)

res = StringVar()
res.set("720p")


label_1 = Label(root, text="YOUTUBE VIDEO DOWNLOADER")
label_2 = Label(root, text="Enter URL here:")

url_entry = Entry(root, width=62)
submit_button = Button(root, text="Download", padx=50, command=lambda:downloadButton(res.get()))


Radiobutton(root, text="360p", variable=res, value="360p",
 command= lambda:radiobutton_clicked).place( x=300, y=100)
Radiobutton(root, text="480p", variable=res, value="480p",
 command= lambda:radiobutton_clicked).place( x=300, y=120)
Radiobutton(root, text="720p", variable=res, value="720p",
 command= lambda:radiobutton_clicked).place( x=300, y=140)


label_1.place(height = 20, x=150, y=10)
label_2.place(height=27, x=10, y=50)
url_entry.place(height=27, x=100, y=50)

submit_button.place(height=27, x=50, y=100)


root.mainloop()


