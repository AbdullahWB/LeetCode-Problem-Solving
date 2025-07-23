"""1695. Maximum Erasure Value

This is a solution for the LeetCode problem 1695: Maximum Erasure Value.
The problem involves finding the maximum sum of a subarray with all unique elements.

**https://leetcode.com/problems/maximum-erasure-value/**

"""

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Initialize variables for the sliding window
        max_score = 0  # Stores the maximum sum found so far
        current_sum = 0  # Stores the sum of elements in the current window
        left = 0  # Left pointer of the sliding window
        seen = set()  # Set to keep track of unique elements in the current window

        # Iterate with the right pointer through the array
        for right in range(len(nums)):
            # Get the current number at the right pointer
            num = nums[right]

            # If the current number is already in the 'seen' set,
            # it means we have a duplicate in our current window.
            # We need to shrink the window from the left until the duplicate is removed.
            while num in seen:
                # Remove the element at the left pointer from the 'seen' set
                seen.remove(nums[left])
                # Subtract the element at the left pointer from the current sum
                current_sum -= nums[left]
                # Move the left pointer to the right
                left += 1

            # Once the current number 'num' is unique in the window,
            # add it to the 'seen' set and update the 'current_sum'.
            seen.add(num)
            current_sum += num

            # Update the maximum score found so far
            max_score = max(max_score, current_sum)

        return max_score
