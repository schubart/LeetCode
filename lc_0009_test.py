from lc_0009 import Solution


def test_examples():
    s = Solution()
    assert not s.isPalindrome(-11)
    assert s.isPalindrome(0)
    assert s.isPalindrome(1)
    assert s.isPalindrome(9)
    assert s.isPalindrome(11)
    assert not s.isPalindrome(12)
    assert not s.isPalindrome(21)
    assert not s.isPalindrome(-111)
    assert s.isPalindrome(111)
    assert s.isPalindrome(121)
    assert not s.isPalindrome(122)