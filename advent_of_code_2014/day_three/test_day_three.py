#pylint: skip-file

from day_three import santa_tracker, coord_splitter, robo_santa_tracker

def test_santa_tracker():
    assert santa_tracker(">") == [[0,0], [1,0]]
    assert santa_tracker("^>v<") == [[0,0], [0,1], [1,1], [1,0], [0,0]]

def test_coord_splitter():
    assert coord_splitter("^^^") == ["^^","^"]
    assert coord_splitter("><^v^v<>") == [">^^<","<vv>"]
    assert coord_splitter("^v^v^v^v") == ["^^^^","vvvv"]

def test_robo_santa_tracker():
    assert robo_santa_tracker('^v') == 3
    assert robo_santa_tracker('^>v<') == 3
    assert robo_santa_tracker('^v^v^v^v^v') == 11