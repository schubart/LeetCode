class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Reverse string: https://stackoverflow.com/a/931095
        return str(x) == str(x)[::-1]


def test():
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