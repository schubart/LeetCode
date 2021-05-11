from functools import cache
from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def combinations(remaining_amount: int, index: int) -> int:
            # Only one way to make amount 0: Pick no coin.
            if remaining_amount == 0:
                return 1

            # Can't make any amount (other than 0) if there are no coins left.
            if index == len(coins):
                return 0

            # Try picking different numbers of the first coin, recurse.
            coin = coins[index]
            return sum(
                combinations(remaining_amount - coin * number, index + 1)
                for number in range(0, (remaining_amount // coin) + 1)
            )

        return combinations(amount, 0)
