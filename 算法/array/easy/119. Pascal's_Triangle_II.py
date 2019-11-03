"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

#method_1     顺序36ms    空间复杂度：O(k)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle_k = [1]
        for k in range(1, rowIndex+1):
            triangle_k.insert(0, 0)
            for i in range(k):
                triangle_k[i] += triangle_k[i+1]
        return triangle_k

#method_2     倒序36ms    空间复杂度：O(k)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle_k = []
        for i in range(rowIndex+1):
            triangle_k.append(1)
            for j in range(i-1, 0, -1):
                triangle_k[j] += triangle_k[j-1]
        return triangle_k

#mehtod_3     36ms      空间复杂度：O(k)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        triangle_k=[1]
        for i in range(0, rowIndex):
            triangle_k=[1]+[triangle_k[i]+triangle_k[i+1] for i in range(triangle_k.__len__()-1)]+[1]
        return triangle_k
