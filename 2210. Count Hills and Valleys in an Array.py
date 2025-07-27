"""
2210. Count Hills and Valleys in an Array
https://leetcode.com/problems/count-hills-and-valleys-in-an-array
"""


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        for x in nums:
            if len(arr) == 0 or arr[-1] != x:
                arr.append(x)
        nums = arr

        N = len(nums)

        count = 0
        for i in range(1, N - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                count += 1
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                count += 1

        return count
