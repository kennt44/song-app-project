import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Playlist, Song, Genre  # Assuming models are in app/models.py

# Database setup
engine = create_engine('sqlite:///music_player.db')
Session = sessionmaker(bind=engine)
session = Session()

def list_playlists():
    playlists = Playlist.get_all(session)
    for playlist in playlists:
        print(f"{playlist.id}: {playlist.name}")

def create_playlist(name):
    Playlist.create(session, name)
    print(f"Playlist '{name}' created.")

def delete_playlist(playlist_id):
    Playlist.delete(session, playlist_id)
    print(f"Playlist with ID {playlist_id} deleted.")

def list_songs():
    songs = Song.get_all(session)
    for song in songs:
        print(f"{song.id}: {song.title} - Playlist: {song.playlist.name} - Genre: {song.genre.name}")

def create_song(title, filepath, playlist_id, genre_id):
    Song.create(session, title, filepath, playlist_id, genre_id)
    print(f"Song '{title}' created.")

def delete_song(song_id):
    Song.delete(session, song_id)
    print(f"Song with ID {song_id} deleted.")

def list_genres():
    genres = Genre.get_all(session)
    for genre in genres:
        print(f"{genre.id}: {genre.name}")

def create_genre(name):
    Genre.create(session, name)
    print(f"Genre '{name}' created.")

def delete_genre(genre_id):
    Genre.delete(session, genre_id)
    print(f"Genre with ID {genre_id} deleted.")

def main():
    parser = argparse.ArgumentParser(description="Music Player CLI")
    parser.add_argument('action', choices=['list', 'create', 'delete', 'find'], help="Action to perform")
    parser.add_argument('entity', choices=['playlist', 'song', 'genre'], help="Entity to perform action on")
    parser.add_argument('id', type=int, nargs='?', help="ID of the entity")
    parser.add_argument('name', type=str, nargs='?', help="Name for creation")
    parse
