#pylint: skip-file

from day_five import extract_rules, extract_sequences, valid_rule, valid_sequence, find_middle, correct_sequence

def test_rule_extractor():
    assert extract_rules('93|53') == [[93,53]]
    assert sorted(extract_rules('''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47''')) == sorted([
[47,53],
[97,13],
[97,61],
[97,47],
[75,29],
[61,13],
[75,53],
[29,13],
[97,29],
[53,29],
[61,53],
[97,53],
[61,29],
[47,13],
[75,47],
[97,75],
[47,61],
[75,61],
[47,29],
[75,13],
[53,13]])

def test_sequences_extractor():
    assert extract_sequences('75,47,61,53,29') == [[75,47,61,53,29]]
    assert extract_sequences('''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47''') == [
    [75,47,61,53,29],
[97,61,53,29,13],
[75,29,13],
[75,97,47,61,53],
[61,13,29],
[97,13,75,29,47]
]

def test_valid_rule():
    assert valid_rule([23,24,57,98,25],[24,25])
    assert valid_rule([23,24,57,98,25],[77,78])
    assert not valid_rule([23,24,57,98,25],[57,24])
    assert not valid_rule([23,24,57,98,25],[25,98])

def test_valid_sequence():
    assert valid_sequence([23,24,57,98,25],[[24,25],[23,98]])
    assert valid_sequence([23,24,57,98,25],[[24,25],[12,11]])
    assert valid_sequence([23,24,57,98,25],[[20,57],[44,23]])
    assert not valid_sequence([23,24,57,98,25],[[10,56],[57,23]])

def test_find_middle():
    assert find_middle([13,22,24]) == 22
    assert find_middle([11,10,11,20,24]) == 11

def test_correct_sequence():
    assert correct_sequence([75,97,47,61,53],[97,75]) == [97,75,47,61,53]
    assert correct_sequence([61,13,29],[29,13]) == [61,29,13]
    assert correct_sequence([97,13,75,29,47],[29,13]) == [97,29,75,13,47]
    assert correct_sequence([97,29,75,13,47],[47,13]) == [97,29,75,47,13]
    assert correct_sequence([97,29,75,47,13],[47,29]) == [97,47,75,29,13]
    