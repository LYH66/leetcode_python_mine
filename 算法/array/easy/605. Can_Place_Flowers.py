"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""

# method_1    一般化方法，避免扩展列表（98%）   最优，泛化能力最强   O(n), O(1)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if l < 2: 
            return n == 0 or flowerbed[0] == 0 == n-1 # 特殊情况判定，花圃数组不为空
        n_flow = 0
        count = 1
        for i in range(1, l):
            if flowerbed[i-1] == flowerbed[i]:
                count += 1
            else:
                n_flow += (count // 2)
                count = 0
        n_flow += (count+1) // 2
        return n_flow >= n

# method_2    利用python列表可拼接的特性，扩展列表，将首尾特殊情况一般化（99%）
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        n_flow = count = 0
        for i in range(1, len(flowerbed)):
            if flowerbed[i-1] == flowerbed[i]:
                count += 1
            else:
                n_flow += (count // 2)
                count = 0
        n_flow += count // 2
        return n_flow >= n

# method_3    抽取可种花地的模式作为判断条件——连续三个零即可种花（90%）
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(2, len(flowerbed)):
            if flowerbed[i] == flowerbed[i-1] == flowerbed[i-2] == 0:   #索引、判断步骤冗余
                n -= 1
                flowerbed[i-1] = 1
        return n <= 0








