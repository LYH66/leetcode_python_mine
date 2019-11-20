"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:
0 ≤ N ≤ 30.
"""

# method_1    动态规划，非递归（94%）   O(n), O(1)
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        f1, f2 = 0, 1
        while N > 1:
            f2, f1 = f1+f2, f2
            N -= 1
        return f2

# method_2    列表存储，空间换时间（98%）   O(n), O(n)
class Solution:
    def fib(self, N: int) -> int:
        A=[0]*31
        A[0]=0
        A[1]=1
        for i in range(2,N+1):
            A[i]=A[i-1]+A[i-2]
        return A[N]










