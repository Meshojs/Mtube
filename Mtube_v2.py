from pytube import *
import pytube as p
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from time import sleep

def main():
    BG = "#171717"
    FGW = "#EEEEEE"
    WIN = Tk()
    WIN.title("Mtube - Youtube Videos Downloader")
    WIN.geometry("400x600")
    WIN.configure(bg=BG)
    WIN.resizable(0, 0)

    EMO  = Label(WIN, text="🎧", fg="#76ABAE", bg=BG, font="Helvetica 40 bold")
    HEADER = Label(WIN, text="Mtube", fg=FGW, bg=BG, font="Helvetica 40 bold")
    EMO.pack(pady=25)
    HEADER.pack()
    LINK_LABLE = Label(
        WIN, text="Put your link", fg=FGW, bg=BG, font="Helvetica 10 bold"
    )
    LINK_LABLE.pack(pady=5)
    # INPUT
    INPUT = Entry(
        WIN,
        width=40,
        bg="#222",
        fg=FGW,
        border=1,
        highlightcolor=FGW,
        font="Helvetica 12 bold",
    )
    INPUT.pack()
    # resolution
    CHOICES = ["360", "480", "720"]
    variable = StringVar(WIN)
    variable.set(CHOICES[0])
    RESOLUTION = OptionMenu(WIN, variable, *CHOICES)
    RESOLUTION.pack(pady=10)

    def download_audio():
        AUD = INPUT.get()
        if AUD == "": 
            messagebox.showinfo("Info","put the link :) ")
        else : 
            put_link = p.YouTube(AUD)
            MPThree = put_link.streams.get_audio_only()
            sleep(0.4)
            MPThree.download()
            messagebox.showinfo("!","The Audio has been successfully Downloaded")

    def download_video():
        reso = variable.get()
        LINK = INPUT.get()
        if LINK == "": 
            messagebox.showinfo("Info","really!? without a link ?")
        else : 
            YT = p.YouTube(LINK)
            VID = YT.streams.get_by_resolution(f"{reso}p")
            sleep(0.4)
            VID.download()
            messagebox.showinfo("!","The Video has been successfully Downloaded")

    
    BTN = Button(
        WIN,
        highlightbackground="#37d3ff",
        text="Download Video",
        fg="white",
        bg="#76ABAE",
        padx=20,
        pady=6,
        font="Helvetica 10 bold",
        command=download_video,
    )
    BTN.pack(pady=10)
    AUD_BTN = Button(
        WIN,
        text="Download Audio MP3",
        fg="white",
        bg="#222",
        pady=6,
        padx=20,
        font="Helvetica 10 bold",
        command=download_audio,
        border=1,
        
        
    )
    AUD_BTN.pack(pady=5)
    DONE = Label(WIN, text="", fg=FGW, bg=BG, font="Helvetica 12 bold")
    DONE.pack(pady=10)
    COPY_RIGHT = Label(
        WIN, text="Made by @Mashary", fg="#222", bg=BG, font="Helvetica 12 bold"
    )
    COPY_RIGHT.pack(pady=70)
    WIN.mainloop()


if __name__ == "__main__":
    main()
