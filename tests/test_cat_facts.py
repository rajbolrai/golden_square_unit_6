from lib.cat_facts import *
from unittest.mock import Mock

def test_get_cat_fact_output_fact():
    request_mock = Mock()
    cat_fact = CatFacts(request_mock)
    
    request_mock.get().json.return_value = {"fact" : "tiger is a big cat"}
    assert cat_fact.provide() == "Cat fact: tiger is a big cat"