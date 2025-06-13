from lib.music_library import *
from unittest.mock import Mock


"""
add track 
return list of track
"""
def test_add_single_track():
    obj_music_history = MusicLibrary()
    fake_track = Mock()
    obj_music_history.add(fake_track)
    assert obj_music_history.tracks == [fake_track]

"""
Given mock tracks
search method returns found
"""
def test_search_for_single_track_with_mocks():
    obj_music_history = MusicLibrary()
    fake_track = Mock()
    fake_track.matches.return_value = True
    obj_music_history.add(fake_track)
    assert obj_music_history.search("hello") == [fake_track]

"""
Given mock tracks
search method returns found
"""
def test_search_for_multiple_track_with_mocks():
    obj_music_history = MusicLibrary()
    fake_track_1 = Mock()
    fake_track_1.matches.return_value = True
    obj_music_history.add(fake_track_1)
    
    fake_track_2 = Mock()
    fake_track_2.matches.return_value = True
    obj_music_history.add(fake_track_2)
    
    fake_track_3 = Mock()
    fake_track_3.matches.return_value = True
    obj_music_history.add(fake_track_3)
    assert obj_music_history.search("hello") == [fake_track_1, fake_track_2, fake_track_3]
    