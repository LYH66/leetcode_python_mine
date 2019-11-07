"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

# method_1    众数的通用求法，利用字典编号存储排序，模拟哈希过程（216ms）
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        elem_appear_times = {}
        
        for i in nums:
            if i in elem_appear_times.keys():     # elem_appear_times.get(i)
                elem_appear_times[i] += 1
            else:
                elem_appear_times[i] = 1
        elem_appear_times = sorted(elem_appear_times, key=elem_appear_times.__getitem__)
        maj_elem = elem_appear_times[-1]
        
        return maj_elem

# method_2    通用求法，但由于利用list内置函数count()计数，需要多次遍历list，时间复杂度较高（312ms）
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return  max([(nums.count(i),i) for i in set(nums)], key=lambda x: x[0])[1]



# method_3    排序，针对题述特定条件求众数（196ms）
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #return sorted(nums)[(len(nums)//2)]
        nums.sort()
        return nums[int(len(nums)/2)]
    
# method_4    Boyer-Moore 投票算法, 针对题述的特定条件（212ms）
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate        # 众数数量大于所有其他元素，最后一定是众数


