"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

#method_1     暴力循环（36ms）    时间复杂度：O(numRows^2) 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            triangle.append([1 for _ in range(i+1)])
            if i > 1:
                for j in range(1, i):
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j] 
        return triangle

#method_2     40ms
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 处理0, 1的特殊情况
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        # 从第二行开始, 数组两边都是1
        r = [[1]] + [[1, 1] for _ in range(numRows - 1)]
        # 第i行
        for i in range(2, numRows):
            # 第i行的第j个元素, 等于上一行的j, j + 1的元素之和
            for j in range(len(r[i - 1]) - 1):
                r[i].insert(j + 1, r[i - 1][j] + r[i - 1][j + 1])
        return r
