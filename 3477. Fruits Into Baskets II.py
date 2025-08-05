class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        F = len(fruits)
        B = len(baskets)

        used = [False] * B
        count = 0

        for i in range(F):
            for j in range(B):
                if not used[j] and fruits[i] <= baskets[j]:
                    used[j] = True
                    break
            else:
                count += 1
        return count
