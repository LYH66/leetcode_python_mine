"""
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
 

Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
 

Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
"""

# method_1    动态规划（17%-99%）   O(n), O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return -1
        leftsum = 0
        rightsum = sum(nums)
        for i in range(n):   
            rightsum -= nums[i]
            if leftsum == rightsum:
                return i
            leftsum+=nums[i]
        return -1

# method_2
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == (total - num) / 2:
                return i
            left_sum += num
        return -1


