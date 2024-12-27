#pylint: skip-file

from day_four import hash_converter

def test_hash_converter():
    assert hash_converter('abcdef') == 609043
    assert hash_converter('pqrstuv') == 1048970