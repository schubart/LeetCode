# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def intToRoman(self, num: int) -> str:
        substitutions = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        remainder = num
        result = ""

        for arabic, roman in substitutions:
            count, remainder = divmod(remainder, arabic)
            result += roman * count

        return result
