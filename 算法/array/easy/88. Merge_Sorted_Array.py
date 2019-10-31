"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

#method_1     双指针倒插for（40ms）    时空复杂度：O(m+n), O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        for index in range(m+n-1, -1, -1):
            if i >= 0 and j >= 0:
                if nums1[i] <= nums2[j]:
                    nums1[index] = nums2[j]
                    j -= 1
                else:
                    nums1[index] = nums1[i]
                    i -= 1  
            else:
                break
        nums1[:j+1] = nums2[:j+1]

#method_2     双指针倒插while（44ms）    时空复杂度：O(m+n), O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        index = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
            index -= 1
        nums1[:j+1] = nums2[:j+1]

#method_3     直接合并两数组，再进行排序，但未利用数组有序这一特点（40ms）    
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)



