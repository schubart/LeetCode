from typing import List

from lc_0027 import Solution


def test_examples():
    def validate(nums: List[int], val):
        expected = [n for n in nums if n != val]

        length = Solution().removeElement(nums, val)

        assert sorted(nums[:length]) == sorted(expected)

    validate([3, 2, 2, 3], 3)
    validate([0, 1, 2, 2, 3, 0, 4, 2], 2)
    validate([0, 1, 2, 2, 3, 0, 4, 2], 10)
    validate([], 0)
