from lib.music_library import *
from lib.track import *

"""
add a track
search for an artist that is not in music history
returns empty list
"""
def test_searching_for_track_not_in_music_history_outputs_empty_list():
    obj_music_history = MusicLibrary()
    ob_track_1 = Track("Fazerdaze", "So Easy")
    obj_music_history.add(ob_track_1)
    assert obj_music_history.search("le sserafim") == []
    
"""
add one track
search for that track
returns list with that track
"""
def test_def_searching_for_single_a_track():
    obj_music_history = MusicLibrary()
    ob_track_1 = Track("Fazerdaze", "So Easy")
    obj_music_history.add(ob_track_1)
    assert obj_music_history.search("So Easy") == [ob_track_1]
    
"""
add multiple tracks
search for that track
returns list with that track
"""
def test_def_searching_for_multiple_tracks():
    obj_music_history = MusicLibrary()
    ob_track_1 = Track("Fazerdaze", "So Easy")
    ob_track_2 = Track("Fazerdaze", "In blue")
    obj_music_history.add(ob_track_1)
    obj_music_history.add(ob_track_2)
    assert obj_music_history.search("Fazerdaze") == [ob_track_1, ob_track_2]