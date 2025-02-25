import pytest

from foo_bar_baz import foo_bar_baz

"""
- Lists every number from 1 to n.
- Replaces numbers divisible by 3 with "Foo".
- Replaces numbers divisible by 5 with "Bar".
- Replaces numbers divisible by both 3 and 5 with "Baz".
"""

#Add testcases Here

def test_input_zero():
    assert foo_bar_baz(0) == "" # Nothing should be printed if input is 0.


def test_input_negative():
    assert foo_bar_baz(-6) == "" # Nothing should be printed if input is negative.


def test_divisible_by_only_one_number():
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"


def test_divisible_by_both_numbers():
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"


def test_divisible_by_none():
    assert foo_bar_baz(2) == "1 2"


def test_str_length():
    for i in range(50):
        str = foo_bar_baz(i)
        assert len(str) == i


def test_word_counts():

    for n in range(50): # Loop through range of n values. 
        baz_count = 0
        bar_count = 0
        foo_count = 0
        str = foo_bar_baz(n)
        for j in range(n + 1): # For each n value, count the number of baz, bar, and foo in str.
            if (n % 3 == 0) and (i % 5 == 0):
                baz_count += 1
            elif (n % 3 == 0):
                foo_count += 1
            elif (n % 5 == 0):
                bar_count += 1
        
        # Check that there are correct number of baz, bar, and foos. 
        assert baz_count == str.count("Baz")
        assert bar_count == str.count("Bar")
        assert foo_count == str.count("foo")