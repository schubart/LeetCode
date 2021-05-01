import random
from collections import Counter

from hypothesis import assume
from hypothesis import given
from hypothesis.strategies import booleans
from hypothesis.strategies import characters
from hypothesis.strategies import composite
from hypothesis.strategies import floats
from hypothesis.strategies import integers
from hypothesis.strategies import permutations
from hypothesis.strategies import text


class Solution():
    def isAnagram(self, s: str, t: str) -> bool:

        # Certainly not an anagram if lengths differ.
        if len(s) != len(t):
            return False

        # Build histogram of characters in s.
        frequencies = Counter(s)

        # Discount frequency of every character in t.
        for c in t:
            frequencies[c] -= 1

            # Fail if c was in t more often than in s.
            if frequencies[c] < 0:
                return False

        # Since both strings are same length and there are
        # no excess characters in t, strings must be anagrams.
        return True


def is_anagram(s: str, t: str) -> bool:
    return Solution().isAnagram(s, t)


@composite
def two_strings(draw):
    """Generate two strings. Sometimes they are anagrams of each other"""

    if draw(booleans()):
        # Two random strings.
        return draw(text()), draw(text())
    else:
        # Second string is permutation of first.
        s1 = draw(text())
        s2 = ''.join(draw(permutations(s1)))
        return s1, s2


def test_examples():
    assert is_anagram("", "")

    assert is_anagram("ab", "ab")
    assert is_anagram("ab", "ba")
    assert not is_anagram("ab", "abb")
    assert not is_anagram("ab", "aab")

    assert is_anagram("anagram", "nagaram")
    assert not is_anagram("rat", "car")


@given(text())
def test_every_string_is_anagram_of_its_reverse(s):
    assert is_anagram(s, ''.join(reversed(s)))


@given(text(), floats())
def test_every_string_is_anagram_of_any_of_its_permutations(s, seed):
    random.seed(seed)
    assert is_anagram(s, ''.join(random.sample(s, len(s))))


@given(text())
def test_anagram_relationship_is_reflexive(s):
    assert is_anagram(s, s)


@given(two_strings())
def test_anagram_relationship_is_symmetric(strings):
    s, t = strings
    assert is_anagram(s, t) == is_anagram(s, t)


@given(two_strings())
def test_anagrams_have_same_lengths(strings):
    s, t = strings
    assume(is_anagram(s, t))
    assert len(s) == len(t)


@given(two_strings(), integers(), characters())
def test_replacing_character_in_anagram_breaks_it(strings, number, c):
    s, t = strings
    assume(is_anagram(s, t))
    assume(s)
    position = number % len(s)
    assume(s[position] != c)
    s_ = s[:position] + c + s[position + 1:]
    assert not is_anagram(s_, t)


@given(two_strings())
def test_solution_is_equivalent_to_naive_solution(strings):
    s, t = strings
    assert is_anagram(s, t) == (sorted(s) == sorted(t))
