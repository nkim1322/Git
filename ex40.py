class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
                        
what_you_know = Song(["In a few weeks I will get time \nTo realise it's right before my eyes \nAnd I can take it if it's what I want to do"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

what_you_know.sing_me_a_song()
