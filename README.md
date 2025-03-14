# song-app-project 
# projo kali 

## Description

This is a simple music player application that allows users to create playlists, add songs, and manage their music collection. The app is built using Python, SQLAlchemy for the database management, and Tkinter for the graphical user interface (GUI). It also integrates `pygame` for music playback functionality.

### Key Features
- Create and manage playlists.
- Add songs to playlists.
- Play, pause, stop, and resume music.
- Browse songs within playlists.
- Manage playlists and songs in the database.

## Technologies Used
- Python 3.x
- SQLAlchemy (ORM for database management)
- SQLite (Database)
- Tkinter (GUI Framework)
- Pygame (Music playback)

## Setup

### Prerequisites
Make sure to have Python 3.x installed on your system. You'll also need to install the required dependencies listed in `Pipfile`.

### Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/kennt44/song-app-project.git
    ```

2. Navigate into the project folder:

    ```bash
    cd song-app-project
    ```

3. Create a virtual environment and install the dependencies:

    If you're using `pipenv`, run:

    ```bash
    pipenv install
    ```

    If you prefer `pip` and a `requirements.txt`, you can generate the requirements file from the `Pipfile` by running:

    ```bash
    pipenv lock --requirements > requirements.txt
    ```

    Then install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. After the setup is complete, make sure the `music_player.db` SQLite database is created and the tables are set up. If not, the app will create them automatically when you run it for the first time.

## Usage

### Running the App

To start the app, you can run the `cli.py` file for the command-line interface or use the `tkinter`-based GUI.

#### For the CLI:

```bash
python cli.py
