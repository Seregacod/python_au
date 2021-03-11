## String
+ [Valid Anagram](#Valid Anagram)
+ [Reverse String](#Reverse String)
+ [Reverse Vowels of a String](#Reverse Vowels of a String)
+ [Reverse Words in a String III](#Reverse Words in a String III)
+ [To Lower Case](#To Lower Case)

##Valid Anagram
https://leetcode.com/problems/valid-anagram/
```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        chars = {}
        for i in s:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1
        for x in t:
            if x in chars:
                chars[x] -= 1
            else:
                return False
        for c in chars:
            if chars[c] != 0:
                return False
        return True
```
##Reverse String
https://leetcode.com/problems/reverse-string/
```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()    
```
##Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = list(s)
        i,j = 0, len(s)-1
        while i<j:
            if lst[i] not in "aeiouAEIOU":
                i+=1
            elif lst[j] not in "aeiouAEIOU":
                j-=1
            else:
                lst[i], lst[j] = lst[j], lst[i]
                i+=1
                j-=1
        return "".join(lst)
```
##Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([word[::-1] for word in s.split(' ')])
```
##To Lower Case
https://leetcode.com/problems/to-lower-case/
```python
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        lower = ""
        for i in range(len(str)):
            a = ord(str[i])
            if a >= 65 and a<=90:
                lower+=chr(a+32)
            else:
                lower+=chr(a)
                
        return lower
```