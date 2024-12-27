This is my holiday practice repo
![Test and Lint Workflow](https://github.com/Candice-Bennett/Holiday_Practise/actions/workflows/pytest-pylint.yml/badge.svg)

### Pytest Results
============================= test session starts ==============================
platform linux -- Python 3.11.11, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/runner/work/Holiday_Practise/Holiday_Practise
collected 23 items

advent_of_code_2014/day_five/test_day_five.py ..........                 [ 43%]
advent_of_code_2014/day_four/test_day_four.py .                          [ 47%]
advent_of_code_2014/day_one/test_day_one.py ...                          [ 60%]
advent_of_code_2014/day_three/test_day_three.py ...                      [ 73%]
advent_of_code_2014/day_two/test_day_two.py ......                       [100%]

============================== 23 passed in 1.67s ==============================
### Pylint Results
************* Module advent_of_code_2014.day_three.day_three
advent_of_code_2014/day_three/day_three.py:33:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
************* Module advent_of_code_2014.day_two.day_two
advent_of_code_2014/day_two/day_two.py:27:63: E0606: Possibly using variable 'smallest' before assignment (possibly-used-before-assignment)
advent_of_code_2014/day_two/day_two.py:64:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
advent_of_code_2014/day_two/day_two.py:94:4: C0103: Constant name "total_area" doesn't conform to UPPER_CASE naming style (invalid-name)
advent_of_code_2014/day_two/day_two.py:95:4: C0103: Constant name "total_ribbon" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module advent_of_code_2014.day_one.day_one
advent_of_code_2014/day_one/day_one.py:27:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)

-----------------------------------
Your code has been rated at 9.45/10

