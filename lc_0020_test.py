from lc_0020 import Solution


def test_examples():
    s = Solution()

    assert s.isValid("()")
    assert s.isValid("()[]{}")
    assert not s.isValid("(]")
    assert not s.isValid("([)]")
    assert s.isValid("{[]}")
