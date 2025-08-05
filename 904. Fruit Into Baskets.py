class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)

        f = collections.Counter()
        best = 0

        left = 0

        for right in range(N):
            f[fruits[right]] += 1

            while len(f) > 2:
                f[fruits[left]] -= 1
                if f[fruits[left]] == 0:
                    del f[fruits[left]]

                left += 1

            best = max(best, right - left + 1)

        return best
