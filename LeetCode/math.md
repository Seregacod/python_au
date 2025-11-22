# Math

+ [sqrt(x)](#sqrt(x))
+ [FizzBuzz](#FizzBuzz)
+ [ReverseInteger](#ReverseInteger)
+ [PalindromeNumber](#PalindromeNumber)
+ [Base7](#Base7)
+ [FibonacciNumber](#FibonacciNumber)
+ [LargestPerimeterTriangle](#Largest Perimeter Triangle)
## sqrt(x)
https://leetcode.com/problems/sqrtx/
```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0,  x
        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        return right
```
## FizzBuzz
https://leetcode.com/problems/fizz-buzz/
```python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        n
        ans = []
        for num in range (1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                ans.append('FizzBuzz')
            elif num % 3 == 0:
                ans.append('Fizz')
            elif num % 5 == 0: 
                ans.append('Buzz')
            else:
                ans.append(str(num))
            return ans
```
##ReverseInteger
https://leetcode.com/problems/reverse-integer/
```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        if x >= 0 :
            revstring = string[::-1]
        else:
            temp = string[1:] 
            temp2 = temp[::-1] 
            revstring = "-" + temp2
        return int(revstring)
```
##PalindromeNumber
https://leetcode.com/problems/palindrome-number/
```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        str_1 = str(abs(x))
        str_2 = str_1[::-1]
        if str_1 == str_2:
            return True
        else:
            return False
```
##Base7
https://leetcode.com/problems/base-7/
```python
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        if num == 0:
            return '0'
        negative = False
        if num < 0:
            num = abs(num)
            negative = True
        c = 0
        while num:
            num, c = divmod(num, 7)
            ans = str(c) + ans
        if negative is True:
            return '-' + ans
        return ans
```
##FibonacciNumber
https://leetcode.com/problems/fibonacci-number/
```python
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
```
##LargestPerimeterTriangle
https://leetcode.com/problems/largest-perimeter-triangle/
```python
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
```