from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Setup SQLAlchemy Base
Base = declarative_base()

class Playlist(Base):
    __tablename__ = 'playlists'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # Relationship to the Song model
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

# Initialize the SQLite database
engine = create_engine('sqlite:///music_player.db')

# Create all tables in the database
Base.metadata.create_all(engine)
