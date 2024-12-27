#pylint: skip-file

from day_three import santa_tracker

def test_santa_tracker():
    assert santa_tracker(">") == 2
    assert santa_tracker("^>v<") == 4
    assert santa_tracker("^v^v^v^v^v") == 2