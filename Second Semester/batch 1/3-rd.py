"""
Пойдем от коробок до элементов коробок:
Альбом может содержать в себе песни и исполнителя(исполнителей)
Плейлист содержит в себе песни
Песня содержит в себе исполнителя
Только исполнитель ничего в себе не содержит, получается, можно начать конструировать взаимосвязи с него
"""


class Performer():
    def __init__(self, name:str) -> None:
        self.name = name

class Song():
    def __init__(self, name:str, perfomer) -> None:
        self.name = name
        if isinstance(perfomer, Performer):
            self.performer = perfomer
        elif isinstance(perfomer, tuple):
            self.performer = "Разные исполнители"

class Album():
    def __init__(self, name:str, songs:tuple[Song]) -> None:
        self.name = name
        self.songs = songs
        self.performer = PerformersCheck(songs)

class Playlist():
    def __init__(self, name:str, *songs) -> None:
        self.name=name
        self.songs = list(*songs)
    
    def AddSong(self, *songs):
        for song_sample in songs:
            self.songs.append(song_sample)
    
    def DelSong(self, name):
        for song in self.songs:
            if name == song.name:
                del self.songs[self.songs.index(song)]

def PerformersCheck(list_of_songs:tuple[Song]):
    set_of_performers = set()
    for song in list_of_songs:
        set_of_performers.add(song.performer)
    
    
    if len(list(set_of_performers)) > 1:
        return "Разные исполнители"
    else:
        return list(set_of_performers)[0]
    


testPerformer1 = Performer("Performer1")
testPerformer2 = Performer("Performer1")

testSong1 = Song("Song1", testPerformer1)
testSong2 = Song("Song2", (testPerformer1, testPerformer2))
testSong3 = Song("Song3", testPerformer1)

testAlbum1 = Album("TestAlbum1", (testSong1, testSong3))
testAlbum2 = Album("TestAlbum1", (testSong1, testSong2, testSong3))

testPlaylist = Playlist("testPlaylist")
testPlaylist.AddSong(testSong1, testSong2)
testPlaylist.DelSong(testSong2)


