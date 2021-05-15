from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []

        for char in s:
            # Get corresponding opening paren assuming ``char`` is a closing one.
            opener = {
                ")": "(",
                "]": "[",
                "}": "{",
            }.get(char, None)

            if opener:
                # ``char`` is a closing paren, so top of the stack must be ``opener``.
                if not stack or stack.pop() != opener:
                    return False
            else:
                # ``char`` is not a cosing paren. Trust input, assume it is opening paren.
                stack.append(char)

        # Stack must be empty after consuming ``s``.
        return not stack
