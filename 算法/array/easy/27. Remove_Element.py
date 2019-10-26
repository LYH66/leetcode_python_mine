"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
"""

#method_1   双指针（一头一尾，不改变数组元素组成）
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        for x in range(length):            
            if nums[x] == val:
                while nums[length-1] == val:
                    if x == length-1:
                        return length-1
                    length -= 1
                temp = nums[length-1]
                nums[length-1] = nums[x]
                nums[x] = temp

#method_2   双指针（一头一尾，改变数组元素组成）
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        length = 0
        while length < n:
            if nums[length] == val:
                nums[length] = nums[n-1]
                n -= 1
            else:
                length += 1
        return length

#method_3   双指针（双头，改变数组元素组成）
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        length = 0
        for j in range(n):
            if nums[j] != val:
                nums[length] = nums[j]
                length += 1
        return length
