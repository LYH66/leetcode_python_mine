"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

#method_1    一般解法（最快36ms）：比较运算符中‘>’、‘<’执行效率优于‘==’     时空复杂度：O(n/2), O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1
        while digits[i] > 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
            else:
                digits[i-1] += 1
                i -= 1
        return digits
  
#method_2    时空复杂度：O(n/2), O(1)
class Solution:
   def plusOne(self, digits: List[int]) -> List[int]:
       for i in range(len(digits)-1, -1, -1):
           digits[i] = (digits[i] + 1) % 10
           if digits[i] != 0:
               return digits
       digits.insert(0, 1)
       return digits
 
#method_3    利用字符串和列表之间的转换（36ms）    时空复杂度：O(n), O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sums = 0
        for i in range(len(digits)):
            sums += 10**(len(digits)-1-i)*digits[i]
        sums_str = str(sums + 1)
        return [int(j) for j in sums_str]

#method_4    利用字符串和列表之间的转换（40ms），最简洁（一行代码）      时空复杂度：O(n), O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(j) for j in str(int(''.join('%s' %i for i in digits))+1)]
  
