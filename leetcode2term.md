#Leetcode2term

+[Course Schedule II](#Course Schedule II)
+[Course Schedule](#Course Schedule)
+[Number of Islands](#Number of Islands)
+[Is Graph Bipartite?](#Is Graph Bipartite?)
+[Cheapest Flights Within K Stops](#Cheapest Flights Within K Stops)
+[Shortest Path in Binary Matrix](#Shortest Path in Binary Matrix)
+[Maximum Depth of N-ary Tree](#Maximum Depth of N-ary Tree)
+[Min Stack](#Min Stack)
+[Implement Queue using Stacks](#Implement Queue using Stacks)
+[Implement Stack using Queues](#Implement Stack using Queues)
+[House Robber II](#House Robber II)
+[House Robber](#House Robber)
+[Design Twitter](#Design Twitter)
+[Merge k Sorted Lists](#Merge k Sorted Lists)
+[K Closest Points to Origin](#K Closest Points to Origin)


##Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
```python
from collections import defaultdict, deque
class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []
```
   
   ##Course Schedule
   https://leetcode.com/problems/course-schedule/
```pyhon
   class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(i):
            color[i] = 1
            if i in graph:
                for j in graph[i]:
                    if color[j] == 0:
                        if not dfs(j):
                            return False
                    elif color[j] == 1:
                        return False
            color[i] = 2
            return True
                            
        graph = {}
        for pair in prerequisites:
            if pair[1] in graph:
                graph[pair[1]].add(pair[0])
            else:
                graph[pair[1]] = set([pair[0]])			
        color = [0]*numCourses
        for i in range(numCourses):
            if color[i] == 0:
                if not dfs(i):
                    return False
        return True
```
##Number of Islands
https://leetcode.com/problems/number-of-islands/
```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs_visit(grid, u):
            i, j = u[0], u[1]
            visit.add((i,j))
            if i > 0 and grid[i-1][j] == '1' and (i-1,j) not in visit:
                dfs_visit(grid, (i-1,j))
            if i < height - 1 and grid[i+1][j] == '1' and (i+1,j) not in visit:
                dfs_visit(grid, (i+1,j))
            if j > 0 and grid[i][j-1] == '1' and (i,j-1) not in visit:
                dfs_visit(grid, (i,j-1))
            if j < width - 1 and grid[i][j+1] == '1' and (i,j+1) not in visit:
                dfs_visit(grid, (i,j+1))
        
        if len(grid) == 0:
            return 0
        count = 0
        visit = set()
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1' and (i,j) not in visit:
                    dfs_visit(grid,(i,j))
                    count += 1
        return count
```
##Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/
```python
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(i, graph):
            for n in graph[i]:
                if n in color:
                    if color[n] != (color[i] + 1) % 2:
                        return False
                else:
                    color[n] = (color[i] + 1) % 2
                    if not dfs(n, graph):
                        return False
            return True
            
        if not graph:
            return False
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i, graph):
                    return False
        return True
```
##Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/
```python
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = {}
        for flight in flights:
            if flight[0] in graph:
                graph[flight[0]][flight[1]] = flight[2]
            else:
                graph[flight[0]] = {flight[1]:flight[2]}
        
        rec = {}
        heap = [(0, -1, src)]
        heapq.heapify(heap)
        while heap:
            cost, stops, city = heapq.heappop(heap)
            if city == dst:
                return cost
            if stops == K or rec.get((city, stops), float('inf')) < cost:
                continue
            if city in graph:
                for nei, price in graph[city].items():
                    summ = cost + price
                    if rec.get((nei, stops+1), float('inf')) > summ:
                        rec[(nei, stops+1)] = summ
                        heapq.heappush(heap, (summ, stops+1, nei))
        return -1
```
##Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/
```python
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
	n = len(grid)
	if grid[0][0] or grid[n-1][n-1]:
		return -1
	q = [(0, 0, 1)]
	grid[0][0] = 1
	for i, j, d in q:
		if i == n-1 and j == n-1: return d
		for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
			if 0 <= x < n and 0 <= y < n and not grid[x][y]:
				grid[x][y] = 1
				q.append((x, y, d+1))
	return -1        
```
##Maximum Depth of N-ary Tree
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            res = 0
            for child in root.children:
                res = max(dfs(child), res)
            return res+1
        return dfs(root)
```
##Min Stack
https://leetcode.com/problems/min-stack/
```python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])
                
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
##Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
```python
class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty(


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
##Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
```python
class MyStack(object):

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]
    
    def empty(self):
        return not len(self._queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```
##House Robber II
https://leetcode.com/problems/house-robber-ii/
```python
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev_max = 0
        curr_max = 0
        for i in range(len(nums)-1):
            tmp = curr_max
            curr_max = max(curr_max, prev_max+nums[i])
            prev_max = tmp
        rec = curr_max
        
        prev_max = 0
        curr_max = 0
        for i in range(len(nums)-1, 0, -1):
            tmp = curr_max
            curr_max = max(curr_max, prev_max+nums[i])
            prev_max = tmp
        return max(rec, curr_max)
```
##House Robber
https://leetcode.com/problems/house-robber/
```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev = 0
        curr = 0
        for n in nums:
            prev, curr = curr, max(prev + n, curr)
        return curr
```
##Design Twitter
https://leetcode.com/problems/design-twitter/
```python
class Twitter(object):

    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```
##Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
```
##K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
```python
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(k, points, lambda (x, y): x * x + y * y)
```
  
