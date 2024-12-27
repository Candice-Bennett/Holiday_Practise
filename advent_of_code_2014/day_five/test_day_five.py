#pylint: skip-file

from day_five import validate_vowels, validate_double_letters, validate_bad_string

def test_validate_vowels_positive_case():
    assert validate_vowels('aei')
    assert validate_vowels('xazegov')
    assert validate_vowels('aeiouaeiouaeiou')

def test_validate_vowels_negative_case():
    assert not validate_vowels('aha')
    assert not validate_vowels('pppopppppppppp')
    assert not validate_vowels('the story goes')

def test_validate_double_positive_case():
    assert validate_double_letters('xx')
    assert validate_double_letters('abcdde')
    assert validate_double_letters('aabbccdd')

def test_validate_double_negative_case():
    assert not validate_vowels('aha')
    assert not validate_vowels('testing that this does not work')
    assert not validate_vowels('the story goes')

def test_validate_bad_positive_case():
    assert validate_bad_string('should be fine')
    assert validate_bad_string('this looks okay')
    assert validate_bad_string('no issues here')

def test_validate_bad_negative_case():
    assert not validate_bad_string('ab')
    assert not validate_bad_string('cd')
    assert not validate_bad_string('pq')
    assert not validate_bad_string('xy')
    assert not validate_bad_string('aaaaaabbababababab')
    assert not validate_bad_string('cdddoutsdjkfn')
    assert not validate_bad_string('fqfqfqpqwasddawq')
    assert not validate_bad_string('roxy')