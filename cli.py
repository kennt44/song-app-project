import sys
from sqlalchemy.orm import sessionmaker
from models import engine, Playlist, Song
from faker import Faker

# Initialize session and faker
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

def cli_menu():
    while True:
        print("\n1. Create Playlist\n2. Add Song\n3. Show Playlists\n4. Show Songs\n5. Find Playlist\n6. Find Song\n7. Delete Playlist\n8. Delete Song\n9. Add Fake Data\n10. Exit")
        choice = input("Enter choice: ").strip()

        if choice == '1': create_playlist(input("Enter name: "))
        elif choice == '2': add_song(input("Enter playlist ID: "), input("Enter title: "), input("Enter file path: "))
        elif choice == '3': show_playlists()
        elif choice == '4': show_songs(input("Enter playlist ID: "))
        elif choice == '5': find_playlist(input("Enter name: "))
        elif choice == '6': find_song(input("Enter title: "))
        elif choice == '7': delete_playlist(input("Enter playlist ID: "))
        elif choice == '8': delete_song(input("Enter song ID: "))
        elif choice == '9': add_fake_data()
        elif choice == '10': sys.exit()
        else: print("Invalid option, try again.")

def create_playlist(name):
    session.add(Playlist(name=name))
    session.commit()
    print(f"Playlist '{name}' created.")

def add_song(playlist_id, title, filepath):
    playlist = session.get(Playlist, playlist_id)  # Updated line using session.get()
    if playlist:
        session.add(Song(title=title, filepath=filepath, playlist=playlist))
        session.commit()
        print(f"Song '{title}' added to playlist.")
    else:
        print(f"No playlist found with ID {playlist_id}.")

def show_playlists():
    for playlist in session.query(Playlist).all():
        print(playlist)

def show_songs(playlist_id):
    playlist = session.get(Playlist, playlist_id)  # Updated line using session.get()
    if playlist:
        for song in playlist.songs:
            print(song)
    else:
        print(f"No playlist found with ID {playlist_id}.")

def find_playlist(name):
    playlist = session.query(Playlist).filter(Playlist.name == name).first()
    print(playlist if playlist else f"No playlist found with name '{name}'.")

def find_song(title):
    song = session.query(Song).filter(Song.title == title).first()
    print(song if song else f"No song found with title '{title}'.")

def delete_playlist(playlist_id):
    playlist = session.get(Playlist, playlist_id)  # Updated line using session.get()
    if playlist:
        session.delete(playlist)
        session.commit()
        print(f"Playlist with ID {playlist_id} deleted.")
    else:
        print(f"No playlist found with ID {playlist_id}.")

def delete_song(song_id):
    song = session.get(Song, song_id)  # Updated line using session.get()
    if song:
        session.delete(song)
        session.commit()
        print(f"Song with ID {song_id} deleted.")
    else:
        print(f"No song found with ID {song_id}.")

def add_fake_data():
    for _ in range(5):  # Add 5 fake playlists
        create_playlist(fake.company())
    for playlist in session.query(Playlist).all():
        for _ in range(3):  # Add 3 fake songs per playlist
            add_song(playlist.id, fake.sentence(nb_words=3), fake.file_path(extension="mp3"))
    print("Fake data added.")

if __name__ == "__main__":
    cli_menu()
