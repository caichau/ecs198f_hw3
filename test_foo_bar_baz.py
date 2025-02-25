import pytest

from foo_bar_baz import foo_bar_baz

"""
- Lists every number from 1 to n.
- Replaces numbers divisible by 3 with "Foo".
- Replaces numbers divisible by 5 with "Bar".
- Replaces numbers divisible by both 3 and 5 with "Baz".
"""

#Add testcases Here

# Nothing should be printed if input is 0.
def test_input_zero():
    assert foo_bar_baz(0) == ""

# Nothing should be printed if input is negative.
def test_input_negative():
    assert foo_bar_baz(-6) == ""

def test_divisible_by_only_one_number():
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

def test_divisible_by_both_numbers():
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

