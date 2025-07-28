"""
2044. Count Number of Maximum Bitwise-OR Subsets
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

"""


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        N = len(nums)
        or_sum = 0
        for x in nums:
            or_sum |= x

        count = 0

        def calc(index, current):
            if index == N:
                if current == or_sum:
                    nonlocal count
                    count += 1
                return

            calc(index + 1, current)
            calc(index + 1, current | nums[index])

        calc(0, 0)
        return count
