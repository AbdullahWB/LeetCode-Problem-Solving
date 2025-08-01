"""

118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown below:
https://leetcode.com/problems/pascals-triangle/description/

"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            ans.append([])
            for j in range(i + 1):
                r = 0
                if j < i:
                    r += ans[i - 1][j]
                if j >= 1:
                    r += ans[i - 1][j - 1]
                ans[i].append(r)
        return ans
