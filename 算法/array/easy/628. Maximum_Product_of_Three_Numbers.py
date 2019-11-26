"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

# method_1    排序（20%-77%）   O(nlogn)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[1] < 0:
            return max(abs(nums[0])*abs(nums[1]), nums[-3]*nums[-2])*nums[-1]           
        return nums[-1]*nums[-2]*nums[-3]

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        v1 = nums[-1] * nums[-2] * nums[-3]    
        v2 = nums[0] * nums[1] * nums[-1]      
        return max(v1, v2)

# method_2    直接取最大最小值（99%）   O(n), O(1)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        nums.remove(max2)
        max3 = max(nums)
        
        nums.extend([max1, max2])
        min1 = min(nums)
        nums.remove(min1)
        min2 = min(nums)
        
        return max(max1 * max2 * max3, min1 * min2 * max1)
        
        
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = 2147483647
        min2 = 2147483647
        max1 = -2147483648
        max2 = -2147483648
        max3 = -2147483648
        for one in nums:
            if one > max1:
                max3 = max2
                max2 = max1
                max1 = one
            elif one > max2:
                max3 = max2
                max2 = one
            elif one > max3:
                max3 = one
            
            if one < min1:
                min2 = min1
                min1 = one
            elif one < min2:
                min2 = one

        temp1 = min1 * min2 * max1
        temp2 = max1 * max2 * max3
        return max(temp1, temp2)





