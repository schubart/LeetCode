from lc_0518 import Solution


def test_examples():
    s = Solution()

    assert s.change(0, []) == 1
    assert s.change(1, []) == 0
    assert s.change(5, [1, 2, 5]) == 4
    assert s.change(3, [2]) == 0
    assert s.change(10, [10]) == 1
    assert s.change(500, [2, 7, 13]) == 717
    assert s.change(5000, [11, 24, 37, 50, 63, 76, 89, 102]) == 992951208
