from abc import ABC,abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    @abstractmethod
    def next(self):
        pass

class Playlist:
    def __init__(self):
        self.songs=[]
    def add_song(self,song):
        self.songs.append(song)
    def get_song(self):
        return self.songs
    
class ReversePlaylistIterator(Iterator):
    def __init__(self, playlist):
        self._songs=playlist.get_song()
        self._index = len(self._songs) - 1

    def has_next(self):
        return self._index>=0

    def next(self):
        song = self._songs[self._index]
        self._index -= 1
        return song

if __name__ == "__main__":
    playlist = Playlist()
    playlist.add_song("Shape of You")
    playlist.add_song("Bohemian Rhapsody")
    playlist.add_song("Blinding Lights")
    
    reverse = ReversePlaylistIterator(playlist)
    while reverse.has_next():
        print(reverse.next())