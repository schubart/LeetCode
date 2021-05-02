import roman

from lc_0012 import Solution


def test_examples():
    s = Solution()

    assert s.intToRoman(3) == "III"
    assert s.intToRoman(4) == "IV"
    assert s.intToRoman(9) == "IX"
    assert s.intToRoman(58) == "LVIII"
    assert s.intToRoman(1994) == "MCMXCIV"


def test_against_known_implementation():
    s = Solution()

    for x in range(1, 4000):
        assert s.intToRoman(x) == roman.toRoman(x)
