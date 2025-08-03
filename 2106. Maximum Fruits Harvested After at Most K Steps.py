"""

This is a solution to the problem of maximizing the total fruits harvested after at most k steps.
https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

"""


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        INF = 10**20
        start_fruit = 0
        f1 = []
        for x, t in fruits:
            if x == startPos:
                start_fruit = t
                continue
            f1.append([x, t])

        def calc(fruits):
            N = len(fruits)
            fruits.sort()

            prefix = [(-INF, 0)]
            for x, t in fruits:
                prefix.append((x, t + prefix[-1][1]))

            fruits_left = 0

            pindex = bisect.bisect_left(prefix, (startPos, -1))
            fruits_left = prefix[pindex - 1][1]

            current = bisect.bisect_left(fruits, [startPos, -1])

            best = 0
            f = 0
            for right in range(current, N):
                dist = fruits[right][0] - startPos
                if dist > k:
                    continue

                f += fruits[right][1]

                remaining = k - dist * 2
                left_pos = startPos - remaining

                if left_pos < startPos:
                    lindex = bisect.bisect_right(prefix, (left_pos, -1))
                    fruits_left_now = fruits_left - prefix[lindex - 1][1]
                else:
                    fruits_left_now = 0

                best = max(best, fruits_left_now + f)
            return best

        left_to_right = calc(f1)
        f2 = []
        for x, t in f1:
            f2.append([-x, t])
        f2.sort()
        startPos = -startPos
        right_to_left = calc(f2)
        return max(left_to_right, right_to_left) + start_fruit
