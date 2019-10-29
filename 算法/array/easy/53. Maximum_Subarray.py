"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

#method_1   动态规划    时空复杂度：O(n), O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        sub_sum = 0
        max_sum = 0
        for x in range(n):
            if sub_sum < 0:
                sub_sum = nums[x]
            else:
                sub_sum += nums[x]
            if sub_sum > max_sum:     # max_sum = max(sub_sum, max_sum)
                max_sum = sub_sum
        return max_sum

#method_2   


