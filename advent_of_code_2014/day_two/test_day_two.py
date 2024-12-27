#pylint: skip-file

import pytest
from advent_of_code_2014.day_two.day_two import surface_area, validate_surface_area, convert_data

def test_surface_area_correct():
    assert surface_area('2x3x4') == 58
    assert surface_area('1x1x10') == 43

def test_validate_surface_area_bad_input():

    assert validate_surface_area([1,2,3,4,5]) == False
    assert validate_surface_area(['one',2,3]) == False
    assert validate_surface_area(True,2,3) == False
    assert validate_surface_area('1',2,3) == False

def test_validate_surface_area_good_input():

    assert validate_surface_area([1,2,3]) == True
    assert validate_surface_area([1.1,2.1,3.1]) == True

def test_convert_data_positive():

    assert convert_data