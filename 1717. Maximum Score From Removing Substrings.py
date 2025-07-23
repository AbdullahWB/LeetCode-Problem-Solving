"""

This is a solution for the LeetCode problem 1717: Maximum Score From Removing Substrings.
The problem involves removing substrings "ab" and "ba" from a given string to maximize the score,
which is calculated based on the points assigned to each substring removal.

**https://leetcode.com/problems/maximum-score-from-removing-substrings/description/**

"""


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score = 0

        # Determine which pair to process first (greedy approach)
        if x >= y:
            first_pair = "ab"
            first_points = x
            second_pair = "ba"
            second_points = y
        else:
            first_pair = "ba"
            first_points = y
            second_pair = "ab"
            second_points = x

        # First pass for the higher-scoring pair
        temp_stack = []
        for char in s:
            temp_stack.append(char)
            if len(temp_stack) >= 2:
                if temp_stack[-2] == first_pair[0] and temp_stack[-1] == first_pair[1]:
                    temp_stack.pop()
                    temp_stack.pop()
                    total_score += first_points

        # Prepare remaining characters for the second pass
        remaining_chars = "".join(temp_stack)

        # Second pass for the lower-scoring pair
        final_stack = []
        for char in remaining_chars:
            final_stack.append(char)
            if len(final_stack) >= 2:
                if (
                    final_stack[-2] == second_pair[0]
                    and final_stack[-1] == second_pair[1]
                ):
                    final_stack.pop()
                    final_stack.pop()
                    total_score += second_points

        return total_score
