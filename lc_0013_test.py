import roman

from lc_0013 import Solution


def test_examples():
    s = Solution()

    assert s.romanToInt("III") == 3
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994


def test_against_known_implementation():
    s = Solution()

    for x in range(1, 4000):
        assert s.romanToInt(roman.toRoman(x)) == x
