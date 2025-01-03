#pylint: skip-file

import pytest
from day_two import surface_area, validate_surface_area, convert_data, ribbon_calculator

def test_validate_surface_area_bad_input():

    assert validate_surface_area([1,2,3,4,5]) == False
    assert validate_surface_area(['one',2,3]) == False
    assert validate_surface_area(['1',2,3]) == False


def test_validate_surface_area_good_input():

    assert validate_surface_area([1,2,3]) == True
    assert validate_surface_area([1.1,2.1,3.1]) == True


def test_convert_data_positive():

    assert convert_data('2x3x4') == [2,3,4]
    assert convert_data('1x1x10') == [1,1,10]


def test_convert_data_negative():

    with pytest.raises(ValueError):
        convert_data('abcabc')
    
    with pytest.raises(ValueError):
        convert_data(True)

    with pytest.raises(ValueError):
        convert_data([1,2,3])

    with pytest.raises(ValueError):
        convert_data('1x2x3x4')


def test_surface_area_correct():

    assert surface_area('2x3x4') == 58
    assert surface_area('1x1x10') == 43


def test_ribbon_calculator():

    assert ribbon_calculator('2x3x4') == 34
    assert ribbon_calculator('1x1x10') == 14