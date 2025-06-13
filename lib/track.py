class Track:
    def __init__(self, title, artist):
        # title and artist are both strings
        if type(title) != str or type(artist) != str: raise TypeError("Error: title and artist must be string")
        if title == "" or artist == "": raise Exception("Error: title and artist cannot be empty")
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        if type(keyword) != str: raise TypeError("Error: keyword must be string")
        if keyword == "": raise Exception("Error: keyword cannot be empty" )
        
        if keyword in self.title or keyword in self.artist:return True
        return False
