from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = 0

        while True:
            if any(len(s) <= length or s[length] != strs[0][length] for s in strs):
                break

            length += 1

        return strs[0][:length]
