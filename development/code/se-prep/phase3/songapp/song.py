import pygame
from pygame import mixer
from tkinter import *
import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Setup SQLAlchemy
Base = declarative_base()

class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    songs = relationship('Song', backref='playlist')

    def __repr__(self):
        return f"Playlist(id={self.id}, name={self.name})"


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    filepath = Column(String)
    playlist_id = Column(Integer, ForeignKey('playlists.id'))

    def __repr__(self):
        return f"Song(id={self.id}, title={self.title}, filepath={self.filepath})"


# Initialize the database
engine = create_engine('sqlite:///music_player.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert some data into the database (only for testing)
if not session.query(Playlist).first():
    playlist = Playlist(name='My Playlist')
    session.add(playlist)
    session.commit()

    # Assuming you have a music directory
    os.chdir(r'C:\Users\DELL\Music')
    songs = os.listdir()

    audio_files = [s for s in songs if s.endswith(('.mp3', '.wav', '.flac', '.ogg'))]

    for s in audio_files:
        song = Song(title=s, filepath=os.path.join(os.getcwd(), s), playlist=playlist)
        session.add(song)
    session.commit()

# Functionality for music player
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

# Playlist setup
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
