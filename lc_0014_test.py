from lc_0014 import Solution


def test_examples():
    s = Solution()

    assert s.longestCommonPrefix([""]) == ""
    assert s.longestCommonPrefix(["x"]) == "x"
    assert s.longestCommonPrefix(["x", "x"]) == "x"
    assert s.longestCommonPrefix(["xy", "xz"]) == "x"
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
