"""

2411. Smallest Subarrays With Maximum Bitwise OR
https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

"""


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)
        D = 30

        best = [0] * N
        best[N - 1] = nums[N - 1]
        for i in range(N - 2, -1, -1):
            best[i] = best[i + 1] | nums[i]

        ans = []
        counts = [0] * D
        right = N - 1

        for left in range(N - 1, -1, -1):
            current_or_sum = 0

            for i in range(D):
                if (nums[left] & (1 << i)) > 0:
                    counts[i] += 1
                if counts[i] > 0:
                    current_or_sum |= 1 << i

            current_or_sum = best[left]
            while right > left:
                good = True
                for i in range(D):
                    if (nums[right] & (1 << i)) > 0:
                        if counts[i] == 1:
                            good = False
                if good:
                    for i in range(D):
                        if (nums[right] & (1 << i)) > 0:
                            counts[i] -= 1
                    right -= 1
                else:
                    break

            ans.append(right - left + 1)
        ans.reverse()
        return ans
