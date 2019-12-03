"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

# method_1    字典统计（100%）    O(n), O(n)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = [1, i, i]
            else:
                dic[nums[i]][0] += 1
                dic[nums[i]][2] = i
        max_freq = [0, 0, 0]
        for value in dic.values():
            if value[0] > max_freq[0]:
                max_freq = value
            elif value[0] == max_freq[0]:
                if value[2]-value[1] < max_freq[2]-max_freq[1]:
                    max_freq = value
        return max_freq[2]-max_freq[1]+1



