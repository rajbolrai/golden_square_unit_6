from unittest.mock import Mock
import pytest
from lib.time_error import *


def test_get_server_time_outut_time():
    request_mock = Mock()
    time = Mock()
    
    obj_time = TimeError(request_mock, time)
    
    obj_time.time.return_value = 1711
    request_mock.get().json.return_value = {"unixtime":1715}
    
    assert obj_time._get_server_time() == 1715
    
    
def test_get_error_time_outut_time():
    request_mock = Mock()
    time_mock = Mock()
    
    obj_time = TimeError(request_mock, time_mock)
    
    time_mock.time.return_value = 1711
    request_mock.get().json.return_value = {"unixtime":1715}
    
    assert obj_time.error() == 4
    
    
    