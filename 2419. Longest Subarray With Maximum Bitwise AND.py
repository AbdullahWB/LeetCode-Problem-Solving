"""

2419. Longest Subarray With Maximum Bitwise AND
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)

        streak = 0
        best = 0
        for x in nums:
            if x == mx:
                streak += 1
            else:
                streak = 0
            best = max(best, streak)
        return best
