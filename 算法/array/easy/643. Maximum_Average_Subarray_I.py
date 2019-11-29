"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""

# method_1    子序列求和（70%）     O(n), O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sub = k_sum = sum(nums[0:k])
        for i in range(0, n-k):
            k_sum += nums[i+k] - nums[i]
            max_sub = max(k_sum, max_sub)
        return max_sub / k






