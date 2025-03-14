import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Playlist, Song
from tkinter import *
import pygame
from pygame import mixer

# Initialize the database
engine = create_engine('sqlite:///music_player.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Function for music player
def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    try:
        mixer.music.load(currentsong)
        songstatus.set("Playing")
        mixer.music.play()
    except Exception as e:
        songstatus.set("Error: Cannot Play Song")
        print(f"Error loading song: {e}")

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

# Setup Tkinter
root = Tk()
root.title('Music Player Project')

mixer.init()
songstatus = StringVar()
songstatus.set("choosing")

# ku setup  Playlist 
playlist = Listbox(root, selectmode=SINGLE, bg="DodgerBlue2", fg="white", font=('arial', 15), width=40)
playlist.grid(columnspan=5)

# Fetch songs from the database (instead of the directory)
songs_in_db = session.query(Song).all()
for song in songs_in_db:
    playlist.insert(END, song.filepath)

# Buttons to control the music player
playbtn = Button(root, text="Play", command=playsong)
playbtn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text="Pause", command=pausesong)
pausebtn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
pausebtn.grid(row=1, column=1)

stopbtn = Button(root, text="Stop", command=stopsong)
stopbtn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
stopbtn.grid(row=1, column=2)

Resumebtn = Button(root, text="Resume", command=resumesong)
Resumebtn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
Resumebtn.grid(row=1, column=3)

root.mainloop()
