"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

# method_1  位运算，异或运算（180ms）  O(n), O(1)  通用解法：0^1^2^3^0^1^3 = (0^0)^(1^1)^(3^3)^2 = 0^0^0^2 = 2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

# method_2  数学计算，利用题目的特殊性（152ms）   最快:O(n), O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1) // 2 - sum(nums)



