#! python3
# -*- coding: utf-8 -*-

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def singe_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
                    
bulls_on_parade = Song(["They really around the family",
                        "With pockets full of the shells"])
                        
happy_bday.singe_me_a_song()

bulls_on_parade.singe_me_a_song()