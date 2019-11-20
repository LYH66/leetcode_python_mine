"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

# method_1    通用解法，一次循环（91%）    O(n), O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = count = 0
        for i in nums:
            if i == 0:
                max_num = max(max_num, count)
                count = 0
                continue
            count += 1
        max_num = max(max_num, count)
        return max_num

# method_2
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        slow = -1
        m = 0
        nums.append(0)
        for i in range(len(nums)):
            if nums[i] == 0:
                m = max(m, i-slow-1)
                slow = i
        return m









