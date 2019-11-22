"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""

# method_1    笨办法，循环（89%）
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)*len(nums[0]) == r*c:
            row_list = []
            nums_reshape = []
            for i in nums:
                for j in i:
                    row_list.append(j)
                    if len(row_list) == c:
                        nums_reshape.append(row_list)
                        row_list = [] 
            return nums_reshape
        return nums

# method_2    迭代器yield（89%）
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        def Y(M):
            for R in M:
                yield from R
        if r * c != len(nums) * len(nums[0]):
            return nums
        it = Y(nums)
        return [[next(it) for _ in range(c)] for _ in range(r)]

# method_3  一次循环（100%），利用内置函数itertools.chain()
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        ans=[[0] * c for _ in range(r)]
        i, j = 0, 0
        for num in itertools.chain(*nums):
            ans[i][j] = num
            j += 1
            if j == c:
                j = 0
                i += 1
        return ans






