#Array
+ [Max Consecutive Ones](#Max Consecutive Ones)
+ [Reshape the Matrix](#Reshape the Matrix)
+ [Image Smoother](#Image Smoother)
+ [Flipping an Image](#Flipping an Image)
+ [Transpose Matrix](#Transpose Matrix)
+ [Move Zeroes](#Move Zeroes)
+ [Squares of a Sorted Array](#Squares of a Sorted Array)

##Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_global = 0
        count_cur = 0
        for i in nums:
            if i == 1:
                count_cur += 1
            else:
                if count_cur > count_global:
                    count_global = count_cur
                count_cur = 0
        return max(count_global, count_cur)    
```
##Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/
```python
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        matrix=[]
        one_row=[]
        for i in nums:
            for j in i:
                one_row.append(j)
        if r*c == len(one_row):
            for i in range(0,len(one_row),c):
                matrix.append(one_row[i:i+c])
            return matrix
        else:
            return nums     
```
##Image Smoother
https://leetcode.com/problems/image-smoother/
```python
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in xrange(R):
            for c in xrange(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] /= count

        return ans      
```
##Flipping an Image
https://leetcode.com/problems/flipping-an-image/
```python
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for i in xrange((len(row) + 1) / 2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A     
```
##Transpose Matrix
https://leetcode.com/problems/transpose-matrix/
```python
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in xrange(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
```
##Move Zeroes
https://leetcode.com/problems/move-zeroes/
```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1        
```
##Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
```python
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(x*x for x in nums)
```