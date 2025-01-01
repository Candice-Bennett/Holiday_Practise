#pylint: skip-file

from day_six import part_one_solution, locate_item, comprehend_input

def test_part_one_solution():
    assert len(part_one_solution('''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
''')) == 41
    
def test_locate_officer():
    assert locate_item(comprehend_input(""".....
##...
.....
.....
..^..
....#
"""),'^') == [[4,2]]
    
    assert locate_item(comprehend_input("""...
^..
...
..#
...
...
"""),'^') == [[1,0]]

def test_locate_obstructions():
    assert locate_item(comprehend_input(""".....
##...
.....
.....
..^..
....#
"""),'#') == [[1,0],[1,1],[5,4]]
    assert locate_item(comprehend_input("""...
^..
...
..#
...
...
"""),'#') == [[3,2]]