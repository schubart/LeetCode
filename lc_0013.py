# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def romanToInt(self, s: str) -> int:
        substitutions = [
            ("IV", 4),
            ("IX", 9),
            ("XL", 40),
            ("XC", 90),
            ("CD", 400),
            ("CM", 900),
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("L", 50),
            ("C", 100),
            ("D", 500),
            ("M", 1000),
        ]

        for roman, arabic in substitutions:
            s = s.replace(roman, str(arabic) + ' ')

        return sum(map(int, s.split()))
