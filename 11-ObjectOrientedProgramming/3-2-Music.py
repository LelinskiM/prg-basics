#Performer: Ed Sheeran
#Title:     Hearts Don't Break Around Here
#Album:     Divide
#Year:      2017

#Performer: Queen
#Title:     Bohemian Rhapsody
#Album:     A Night at the Opera
#Year:      1975
# class definition
class Song:
   def __init__(self,Performer,Title,Album,Year):
        self.Performer = Performer
        self.Title = Title
        self.Album = Album
        self.Year = Year


   def __str__(self):
    return f'Performer:{self.Performer}\n,Title: {self.Title}\n,Album: {self.Album}\n,Year: {self.Year}  '

# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

## object usage
print(song1)
print(song2)