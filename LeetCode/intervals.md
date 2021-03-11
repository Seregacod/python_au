#Intervals

+ [Non-overlapping Intervals](#Non-overlapping Intervals)
+ [Merge Intervals](#Merge Intervals)
+ [Insert Interval](#Insert Interval)

##Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
```python
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ans = 0
        currentEnd = float('-inf')

        for interval in sorted(intervals, key=lambda x: x[1]):
            if interval[0] >= currentEnd:
                currentEnd = interval[1]
            else:
                ans += 1
        return ans
```

##Merge Intervals
https://leetcode.com/problems/merge-intervals/
```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
```

##Insert Interval
https://leetcode.com/problems/insert-interval/
```python
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i, n = 0, len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        mI = newInterval;
        while i < n and intervals[i][0] <= newInterval[1]:
            mI[0] = min(mI[0], intervals[i][0])
            mI[1] = max(mI[1], intervals[i][1])
            i += 1
        
        result.append(mI)
        
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
```