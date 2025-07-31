"""

898. Bitwise ORs of Subarrays
https://leetcode.com/problems/bitwise-ors-of-subarrays/

"""


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        N = len(arr)

        seen = set()
        ans = set()

        def go(index, current):
            if index >= N:
                ans.add(current)
                return
            if (index, current) in seen:
                return
            seen.add((index, current))
            ans.add(current)

            go(index + 1, current | arr[index])

        for i in range(N):
            go(i, arr[i])

        return len(ans)
