import os
from pytube import YouTube
import tkinter as tk
from PIL import Image, ImageTk



def HQ():
    entered_text = textentry.get()
    video_URL = entered_text
    video_URL = str(video_URL)
    ytVideo = YouTube(video_URL)  # Video
    videoTitle = ytVideo.title  # Video title
    video = ytVideo.streams.filter()  # filter
    output.insert(tk.END ,videoTitle)
    video = ytVideo.streams.filter(file_extension='mp4')
    output.insert(tk.END, '\nDownloading...')
    video.get_highest_resolution().download()
    output.insert(tk.END, '\nDone!\n')


def LQ():
    entered_text = textentry.get()
    video_URL = entered_text
    video_URL = str(video_URL)
    ytVideo = YouTube(video_URL)  # Video
    videoTitle = ytVideo.title  # Video title
    video = ytVideo.streams.filter()  # filter
    output.insert(tk.END ,videoTitle)
    video = ytVideo.streams.filter(file_extension='mp4')
    output.insert(tk.END, '\nDownloading...')
    video.get_lowest_resolution().download()
    output.insert(tk.END, '\nDone!\n')

def shitQ():
    entered_text = textentry.get()
    video_URL = entered_text
    video_URL = str(video_URL)
    ytVideo = YouTube(video_URL)  # Video
    videoTitle = ytVideo.title  # Video title
    video = ytVideo.streams.filter()  # filter
    output.insert(tk.END ,videoTitle)
    output.insert(tk.END, '\nDownloading...')
    video.get_lowest_resolution().download()
    output.insert(tk.END, '\nDone!\n')

def MP3():
    entered_text = textentry.get()
    video_URL = entered_text
    video_URL = str(video_URL)
    ytVideo = YouTube(video_URL)  # Video
    videoTitle = ytVideo.title  # Video title
    video = ytVideo.streams.filter()  # filter
    output.insert(tk.END ,videoTitle)
    video = ytVideo.streams.get_audio_only()
    output.insert(tk.END, '\nDownloading...')
    video.download()
    output.insert(tk.END, '\nDone!\n')
    video_path = video.get_file_path()
    base = os.path.splitext(video_path)[0]
    os.rename(video_path, base + '.mp3')



root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)
root.title('sus')

#logo
logo = Image.open('YT.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text='Enter the link')
instructions.grid(columnspan=3, column=0, row=1)

#textBox
textentry = tk.Entry(root, width=50, bg='white')
textentry.grid(row=2, column=1)

#submit buttons
tk.Button(root, text='MP4 HQ', width=6, command=HQ).grid(row=0, column=0)
tk.Button(root, text='MP4 LQ', width=6, command=LQ).grid(row=1, column=0)
tk.Button(root, text='SHIT Q', width=6, command=shitQ).grid(row=2, column=0)
tk.Button(root, text='MP3 HQ', width=6, command=MP3).grid(row=3, column=0)

#output box
output = tk.Text(root, width=50,height=6,background='white')
output.grid(row=4, column=1, columnspan=1)

root.mainloop()
