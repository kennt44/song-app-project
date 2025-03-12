# app/db.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

# Initialize the database (SQLite in this case)
engine = create_engine('sqlite:///music_player.db')
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
session = Session()
