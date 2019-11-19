"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

# method_1    利用python特性，集合相减（79%）
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set([x for x in range(1, len(nums)+1)]) - set(nums))

# method_2    鸽巢理论，异或运算（25%）   O(n), O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def swap(nums, index1, index2):
            # 这一步是必要的，否则会使得一个数变成 0
            if index1 == index2:
                return
            nums[index1] = nums[index1] ^ nums[index2]
            nums[index2] = nums[index1] ^ nums[index2]
            nums[index1] = nums[index1] ^ nums[index2]

        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                # 如果不在位置上，并且它将要去的那个位置上的数不等于自己，则交换
                swap(nums, i, nums[i] - 1)

        return [i + 1 for i, num in enumerate(nums) if num != i + 1]
