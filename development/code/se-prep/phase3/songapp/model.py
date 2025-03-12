from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    songs = relationship('Song', back_populates='genre')

    def __repr__(self):
        return f"<Genre(id={self.id}, name={self.name})>"

    # ORM methods
    @classmethod
    def create(cls, session, name):
        genre = cls(name=name)
        session.add(genre)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, genre_id):
        return session.query(cls).filter_by(id=genre_id).first()

    @classmethod
    def delete(cls, session, genre_id):
        genre = cls.find_by_id(session, genre_id)
        if genre:
            session.delete(genre)
            session.commit()

class Playlist(Base):
    __tablename__ = 'playlists'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    songs = relationship('Song', back_populates='playlist')

    def __repr__(self):
        return f"<Playlist(id={self.id}, name={self.name})>"

    # ORM methods
    @classmethod
    def create(cls, session, name):
        playlist = cls(name=name)
        session.add(playlist)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, playlist_id):
        return session.query(cls).filter_by(id=playlist_id).first()

    @classmethod
    def delete(cls, session, playlist_id):
        playlist = cls.find_by_id(session, playlist_id)
        if playlist:
            session.delete(playlist)
            session.commit()

class Song(Base):
    __tablename__ = 'songs'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    playlist_id = Column(Integer, ForeignKey('playlists.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))

    playlist = relationship('Playlist', back_populates='songs')
    genre = relationship('Genre', back_populates='songs')

    def __repr__(self):
        return f"<Song(id={self.id}, title={self.title}, genre={self.genre.name})>"

    # ORM methods
    @classmethod
    def create(cls, session, title, filepath, playlist_id, genre_id):
        song = cls(title=title, filepath=filepath, playlist_id=playlist_id, genre_id=genre_id)
        session.add(song)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, song_id):
        return session.query(cls).filter_by(id=song_id).first()

    @classmethod
    def delete(cls, session, song_id):
        song = cls.find_by_id(session, song_id)
        if song:
            session.delete(song)
            session.commit()
