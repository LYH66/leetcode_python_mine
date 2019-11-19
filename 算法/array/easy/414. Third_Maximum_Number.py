"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

# method_1    利用python特性，去重、排序（74%）
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)
        if n < 3:
            return nums[n-1]
        else:
            return nums[n-3]

# method_2    暴力解法，三次循环（74%）
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        flag = 0

        for i in nums:
            if i>= first:
                first = i
        for i in nums:
            if i>= second and i < first:
                second = i
        
        for i in nums:
            if i>= third and i < second:
                third = i
                flag = 1
        
        if flag == 1:
            return third
        else:
            return first


