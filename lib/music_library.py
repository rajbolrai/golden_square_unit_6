class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.tracks = []

    def add(self, track):
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing
        self.tracks.append(track)

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        matched_track = []
        for i in self.tracks:
            if i.matches(keyword):
                matched_track.append(i)
        return matched_track
