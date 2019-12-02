"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
 
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
 
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""

# method_1    直接循环判断（77%）
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        _M = [[0]*n for _ in M]
        for i in range(m):
            for j in range(n):
                count = 0
                for nr in (i-1, i, i+1):
                    for nc in (j-1, j, j+1):
                        if 0 <= nr < m and 0 <= nc < n:
                            _M[i][j] += M[nr][nc]
                            count += 1
                _M[i][j] //= count
        return _M


# method_2    矩阵四周添加元素，特殊情况一般化（99%）
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        r=len(M)
        c=len(M[0])
        M.insert(0,[-1]*c)
        M.append([-1]*c)
        for i in range(len(M)):
            M[i].insert(0,-1)
            M[i].append(-1)
 
        res=[]
        for i in range(r):
            row=[]
            for j in range(c):
                lst=[M[i][j],M[i][j+1],M[i][j+2],M[i+1][j],M[i+1][j+1],M[i+1][j+2],M[i+2][j],M[i+2][j+1],M[i+2][j+2]]
                n=lst.count(-1)                
                item=int((sum(lst)+n)/(9-n))
                row.append(item)
            res.append(row)
        return res






