from pytube import *
import pytube as p
import tkinter as tk
from tkinter import *


def main():
    BG = "#222831"
    FGW = "#EEEEEE"
    WIN = Tk()
    WIN.title("Mtube - Youtube Videos Downloader")
    WIN.geometry("400x600")
    WIN.configure(bg="#222831")
    WIN.resizable(0, 0)
    EMO = Label(WIN, text="⚡", fg="#31363F", bg=BG, font="Helvetica 50 bold")
    HEADER = Label(WIN, text="Mtube", fg=FGW, bg=BG, font="Helvetica 40 bold")
    EMO.pack(pady=10)
    HEADER.pack()
    LINK_LABLE = Label(
        WIN, text="Put your link", fg=FGW, bg=BG, font="Helvetica 12 bold"
    )
    LINK_LABLE.pack(pady=10)
    # INPUT
    INPUT = Entry(
        WIN,
        width=50,
        bg="#31363F",
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
        put_link = p.YouTube(AUD)
        MPThree = put_link.streams.get_audio_only()
        MPThree.download()
        DONE.configure(text="The Audio has been successfully Downloaded")

    def download_video():
        reso = variable.get()
        LINK = INPUT.get()
        YT = p.YouTube(LINK)
        VID = YT.streams.get_by_resolution(f"{reso}p")
        VID.download()
        DONE.configure(text="The video has been successfully Downloaded")

    BTN = Button(
        WIN,
        text="Download Video",
        fg="white",
        bg="#76ABAE",
        padx=20,
        font="Helvetica 10 bold",
        command=download_video,
    )
    BTN.pack(pady=10)
    AUD_BTN = Button(
        WIN,
        text="Download Audio MP3",
        fg="white",
        bg="#76ABAE",
        padx=20,
        font="Helvetica 10 bold",
        command=download_audio,
    )
    AUD_BTN.pack(pady=5)
    DONE = Label(WIN, text="", fg=FGW, bg=BG, font="Helvetica 12 bold")
    DONE.pack(pady=10)
    COPY_RIGHT = Label(
        WIN, text="Made by @Mashary", fg="#31363F", bg=BG, font="Helvetica 12 bold"
    )
    COPY_RIGHT.pack(pady=60)
    WIN.mainloop()


if __name__ == "__main__":
    main()
