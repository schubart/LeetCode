import random
from collections import Counter

import pytest
from hypothesis import assume
from hypothesis import given
from hypothesis.strategies import booleans
from hypothesis.strategies import composite
from hypothesis.strategies import floats
from hypothesis.strategies import permutations
from hypothesis.strategies import text


class SimpleSolution():
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class OptimizedSolution():
    def isAnagram(self, s: str, t: str) -> bool:

        # Certainly not an anagram if lengths differ.
        if len(s) != len(t):
            return False

        # Build histogram of characters in s.
        frequencies = Counter(s)

        # Discount frequency of every character in t.
        for c in t:
            frequencies[c] -= 1

            # Fail early if c was in t more often than in s.
            if frequencies[c] < 0:
                return False

        # Anagram if every character count went back down to zero.
        return all(f == 0 for f in frequencies.values())


@pytest.fixture(
    scope='module',
    params=[SimpleSolution(), OptimizedSolution()],
    ids=lambda solution: type(solution))
def solution(request):
    """Test all solutions"""

    return request.param


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


def test_examples(solution):
    assert solution.isAnagram("", "")

    assert solution.isAnagram("ab", "ab")
    assert solution.isAnagram("ab", "ba")
    assert not solution.isAnagram("ab", "abb")
    assert not solution.isAnagram("ab", "aab")

    assert solution.isAnagram("anagram", "nagaram")
    assert not solution.isAnagram("rat", "car")


@given(text())
def test_every_string_is_anagram_of_its_reverse(solution, string):
    assert solution.isAnagram(string, ''.join(reversed(string)))


@given(text(), floats())
def test_every_string_is_anagram_of_any_of_its_permutations(solution, string, seed):
    random.seed(seed)
    assert solution.isAnagram(string, ''.join(random.sample(string, len(string))))


@given(text())
def test_anagram_relationship_is_reflexive(solution, string):
    assert solution.isAnagram(string, string)


@given(two_strings())
def test_anagram_relationship_is_symmetric(solution, strings):
    assert solution.isAnagram(strings[0], strings[1]) == solution.isAnagram(strings[1], strings[0])


@given(two_strings())
def test_anagrams_have_same_lengths(solution, strings):
    assume(solution.isAnagram(strings[0], strings[1]))
    assert len(strings[0]) == len(strings[1])


solution2 = solution


@given(two_strings())
def test_solutions_are_equivalent(solution, solution2, strings):
    assert solution.isAnagram(strings[0], strings[1]) == solution2.isAnagram(strings[0], strings[1])
