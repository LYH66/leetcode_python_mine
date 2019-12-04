"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
## 26进制问题

# method_1    （99%）
class Solution:
    def convertToTitle(self, n: int) -> str:
        title = ''
        r = n
        while r > 0:
            title = chr(65 + (r-1)%26) + title
            r = (r-1) // 26
        return title


# method_2  （99%）
class Solution:
    def convertToTitle(self, n: int) -> str:
        title = ''
        r = (n, 0)
        while r[0] > 0:
            r = divmod(r[0]-1, 26)   
            title = chr(65 + r[1]) + title
        return title

