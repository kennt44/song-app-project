import sys
from sqlalchemy.orm import sessionmaker
from models import engine, Playlist, Song

Session = sessionmaker(bind=engine)
session = Session()

def cli_menu():
    while True:
        print("1. Create Playlist")
        print("2. Add Song to a Playlist")
        print("3. Display All Playlists")
        print("4. Display All Songs in a Playlist")
        print("5. Find Playlist by Name")
        print("6. Find Song by its Title")
        print("7. Delete Playlist")
        print("8. Delete Song")
        print("9. Exit")
        
        choice = input("Enter choice yako: ")
        
        if choice == '1':
            name = input("Enter playlist name: ")
            create_playlist(name)
        elif choice == '2':
            playlist_id = input("Enter playlist ID: ")
            title = input("Enter song title: ")
            filepath = input("Enter song filepath: ")
            add_song_to_playlist(playlist_id, title, filepath)
        elif choice == '3':
            display_all_playlists()
        elif choice == '4':
            playlist_id = input("Enter playlist ID: ")
            display_all_songs_in_playlist(playlist_id)
        elif choice == '5':
            name = input("Enter playlist name: ")
            find_playlist_by_name(name)
        elif choice == '6':
            title = input("Enter song title: ")
            find_song_by_title(title)
        elif choice == '7':
            playlist_id = input("Enter playlist ID: ")
            delete_playlist(playlist_id)
        elif choice == '8':
            song_id = input("Enter song ID: ")
            delete_song(song_id)
        elif choice == '9':
            print("Exiting...")
            sys.exit()
        else:
            print("ime kata . jaribu tena .")

def create_playlist(name):
    playlist = Playlist(name=name)
    session.add(playlist)
    session.commit()
    print(f"Playlist '{name}' created.")

def add_song_to_playlist(playlist_id, title, filepath):
    playlist = session.query(Playlist).filter(Playlist.id == playlist_id).first()
    if playlist:
        song = Song(title=title, filepath=filepath, playlist=playlist)
        session.add(song)
        session.commit()
        print(f"Song '{title}' added to playlist '{playlist.name}'.")
    else:
        print(f"No playlist found with ID {playlist_id}.")

def display_all_playlists():
    playlists = session.query(Playlist).all()
    for playlist in playlists:
        print(playlist)

def display_all_songs_in_playlist(playlist_id):
    playlist = session.query(Playlist).filter(Playlist.id == playlist_id).first()
    if playlist:
        for song in playlist.songs:
            print(song)
    else:
        print(f"No playlist found with ID {playlist_id}.")

def find_playlist_by_name(name):
    playlist = session.query(Playlist).filter(Playlist.name == name).first()
    if playlist:
        print(playlist)
    else:
        print(f"No playlist found with name '{name}'.")

def find_song_by_title(title):
    song = session.query(Song).filter(Song.title == title).first()
    if song:
        print(song)
    else:
        print(f"No song found with title '{title}'.")

def delete_playlist(playlist_id):
    playlist = session.query(Playlist).filter(Playlist.id == playlist_id).first()
    if playlist:
        session.delete(playlist)
        session.commit()
        print(f"Playlist with ID {playlist_id} deleted.")
    else:
        print(f"No playlist found with ID {playlist_id}.")

def delete_song(song_id):
    song = session.query(Song).filter(Song.id == song_id).first()
    if song:
        session.delete(song)
        session.commit()
        print(f"Song with ID {song_id} deleted.")
    else:
        print(f"No song found with ID {song_id}.")

# Run the CLI menu
if __name__ == "__main__":
    cli_menu()
