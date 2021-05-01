from collections import Counter


class Solution():
    def isAnagram(self, s: str, t: str) -> bool:

        # Certainly not an anagram if lengths differ.
        if len(s) != len(t):
            return False

        # Build histogram of characters in s.
        frequencies = Counter(s)

        # Discount frequency of every character in t.
        for c in t:
            frequencies[c] -= 1

            # Fail if c was in t more often than in s.
            if frequencies[c] < 0:
                return False

        # Since both strings are same length and there are
        # no excess characters in t, strings must be anagrams.
        return True
