"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

# method_1    排序，首尾比较（95%）    O(nlogn), O(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sort = nums
        nums_sort = sorted(nums_sort)
        n = len(nums)
        for i in range(n):
            if nums[i] != nums_sort[i]:
                for j in range(n-1, i, -1):
                    if nums[j] != nums_sort[j]:
                        return j-i+1
        return 0

# method_2    两次循环（100%）   O(n), O(1)   
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        max_num=nums[0]
        right=0
        for i in range(n):
            if(nums[i]>=max_num):
                max_num=nums[i]
            else:
                right=i   #右侧临界点处最后一次更新right
        left=n
        min_num=nums[-1]
        for i in range(n-1,-1,-1):
            if(nums[i]<=min_num):
                min_num=nums[i]
            else:
                left=i    #左侧临界点处最后一次更新left
        return right-left+1 if(right-left+1 >0) else 0



