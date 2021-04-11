from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dest = 0
        for n in nums:
            if n != val:
                nums[dest] = n
                dest += 1

        return dest


def test():
    s = Solution()

    def validate(nums: List[int], val):
        expected = [n for n in nums if n != val]

        length = s.removeElement(nums, val)

        assert sorted(nums[:length]) == sorted(expected)

    validate([3, 2, 2, 3], 3)
    validate([0, 1, 2, 2, 3, 0, 4, 2], 2)
    validate([0, 1, 2, 2, 3, 0, 4, 2], 10)
    validate([], 0)
