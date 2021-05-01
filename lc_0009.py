# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Reverse string: https://stackoverflow.com/a/931095
        return str(x) == str(x)[::-1]
