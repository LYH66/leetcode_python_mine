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

#method_2   分冶法   时空复杂度：O(nlogn), O(logn)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            print(tmp, max_r)
            max_r = max(tmp, max_r)
            print("ww",tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)

