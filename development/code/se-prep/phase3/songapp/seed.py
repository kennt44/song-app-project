# seed.py
from app.db import Song, Playlist, engine
from sqlalchemy.orm import sessionmaker
import os

Session = sessionmaker(bind=engine)
session = Session()

# Create a playlist if it doesn't exist
if not session.query(Playlist).first():
    playlist = Playlist(name='My Playlist')
    session.add(playlist)
    session.commit()

    # Add songs from a local directory (replace with your actual path)
    os.chdir(r'C:\Users\DELL\Music')  # Change this to your music folder
    songs = os.listdir()
    audio_files = [s for s in songs if s.endswith(('.mp3', '.wav', '.flac', '.ogg'))]

    for song_file in audio_files:
        song = Song(title=song_file, filepath=os.path.join(os.getcwd(), song_file), playlist=playlist)
        session.add(song)
    session.commit()

print("Database seeded successfully!")
