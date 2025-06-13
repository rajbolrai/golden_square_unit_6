from lib.track import *
import pytest
"""
given non-string title and artist
raise type error
"""
def test_given_non_string_title_and_artist_raise_error():
    with pytest.raises(TypeError) as err:
        Track({}, 2123)
    assert str(err.value) == "Error: title and artist must be string" 
    
    """
given empty title and artist
raise exception
"""
def test_given_empty_string_title_and_artist_raise_expection():
    with pytest.raises(Exception) as err:
        Track("", "")
    assert str(err.value) == "Error: title and artist cannot be empty" 
    
""""  
given empty keyword
raise exception
"""
def test_given_empty_string_keyword_raise_expection():
    obj_track = Track("hello", "word")
    with pytest.raises(Exception) as err:
        obj_track.matches("")
    assert str(err.value) == "Error: keyword cannot be empty" 
    
""""  
given non-string keyword
raise type error
"""
def test_given_non_string_keyword_raise_type_error():
    obj_track = Track("hello", "word")
    with pytest.raises(Exception) as err:
        obj_track.matches(1231)
    assert str(err.value) == "Error: keyword must be string" 
    
"""
if keyword in title 
return true
"""
def test_found_matching_title_output_true():
    obj_track = Track("hello", "word")
    assert obj_track.matches("hello") == True

"""
if keyword not in title 
return false
"""
def test_not_found_matching_title_output_false():
    obj_track = Track("hello", "word")
    assert obj_track.matches("zello") == False
    
"""
if keyword found in artist  
return true
"""
def test_found_matching_artist_output_true():
    obj_track = Track("hello", "world")
    assert obj_track.matches("world") == True

"""
if keyword not found in artist  
return false
"""
def test_not_found_matching_artist_output_false():
    obj_track = Track("hello", "world")
    assert obj_track.matches("zorld") == False
    