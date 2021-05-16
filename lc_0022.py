from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(opening: int, closing: int) -> List[str]:
            if not opening and not closing:
                yield ""

            if opening:
                for rest in generate(opening - 1, closing + 1):
                    yield "(" + rest

            if closing:
                for rest in generate(opening, closing - 1):
                    yield ")" + rest

        return list(generate(n, 0))
