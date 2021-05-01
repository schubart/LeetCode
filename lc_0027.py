from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dest = 0
        for n in nums:
            if n != val:
                nums[dest] = n
                dest += 1

        return dest
