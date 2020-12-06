# Math

+ [sqrt(x)](#sqrt(x))
+ [FizzBuzz](#FizzBuzz)
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