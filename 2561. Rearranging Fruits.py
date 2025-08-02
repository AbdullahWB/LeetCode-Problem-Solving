"""

2561. Rearranging Fruits
You are given two baskets of fruits, represented as lists of integers where each integer represents the cost of a fruit. The goal is to make the two baskets equal by swapping fruits between them at the minimum cost.
https://leetcode.com/problems/rearranging-fruits/description/

"""

import collections
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Calculates the minimum cost to make two fruit baskets equal.
        The method uses a greedy approach based on the costs of fruits.
        """

        # Step 1: Count all fruits and find the global minimum cost in a single pass.
        # This is more efficient than calling min() on each list separately.
        count1 = collections.Counter(basket1)
        count2 = collections.Counter(basket2)
        total_counts = count1 + count2

        mn = float("inf")
        for fruit_cost in basket1:
            mn = min(mn, fruit_cost)
        for fruit_cost in basket2:
            mn = min(mn, fruit_cost)

        # Step 2: Check if it's possible to make the baskets equal.
        # This requires the total count of each fruit to be an even number.
        for fruit_cost, total_count in total_counts.items():
            if total_count % 2 != 0:
                return -1

        # Step 3: Identify the fruits that are "in the wrong basket."
        # A fruit is in the wrong basket if its count is greater than half of the total count
        # for that fruit type. We collect all these fruits into a single list.
        fruits_to_swap_out = []
        for fruit_cost, total_count in total_counts.items():
            half_total = total_count // 2

            # Fruits that need to move out of basket1
            diff_from_b1 = count1.get(fruit_cost, 0) - half_total
            if diff_from_b1 > 0:
                fruits_to_swap_out.extend([fruit_cost] * diff_from_b1)

            # Fruits that need to move out of basket2
            diff_from_b2 = count2.get(fruit_cost, 0) - half_total
            if diff_from_b2 > 0:
                fruits_to_swap_out.extend([fruit_cost] * diff_from_b2)

        # Step 4: Sort the list to apply the greedy strategy.
        # To minimize cost, we must perform swaps involving the cheapest fruits first.
        fruits_to_swap_out.sort()

        # Step 5: Calculate the minimum cost.
        # We need to perform `len(fruits_to_swap_out) // 2` swaps.
        # We pair the cheapest fruits to be moved with each other.
        # The cost of a single swap is the minimum of two options:
        # a) a direct swap of the two fruits (cost is min(fruit_a, fruit_b)).
        # b) an indirect swap using the globally cheapest fruit (cost is 2 * mn).
        # We greedily choose the cheaper option for each pair.

        score = 0
        num_swaps_needed = len(fruits_to_swap_out) // 2

        for i in range(num_swaps_needed):
            # The fruits in the first half of the sorted list are the cheapest ones to be moved.
            # We pair them with the fruits in the second half of the list.
            # However, a simpler and equivalent greedy observation is that the cost to "fix"
            # the `i`-th cheapest fruit is `min(its_cost, 2 * mn)`.
            fruit_cost = fruits_to_swap_out[i]
            score += min(fruit_cost, 2 * mn)

        return score
