#Trees
+ [Maximum Depth of Binary Tree](#Maximum Depth of Binary Tree)
+ [Binary Tree Inorder Traversal](#Binary Tree Inorder Traversal)
+ [Invert Binary Tree](#Invert Binary Tree)
+ [Binary Search Tree Iterator](#Binary Search Tree Iterator)
+ [Binary Tree Level Order Traversal](#Binary Tree Level Order Traversal)
+ [Kth Smallest Element in a BST](#Kth Smallest Element in a BST)
+ [Validate Binary Search Tree](#Validate Binary Search Tree)
+ [Symmetric Tree](#Symmetric Tree)
##Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))    
```
##Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorderTraversalHelper( root, res )
        return res
    
    
    def inorderTraversalHelper(self, node, res):
        if node:
            if node.left:
                self.inorderTraversalHelper(node.left, res)
                
            res.append(node.val)
            
            if node.right:
                self.inorderTraversalHelper(node.right, res)        
```
##Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
        return root      
```
##Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        self.inorder(root)
    def inorder(self,root):
        if not root:
            return 
        self.inorder(root.right)
        self.stack.append(root.val)
        self.inorder(root.left)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)>0

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
##Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        queue = []
        queue.append(root)
        
        while queue:
            level_size = len(queue)
            level = []
            for i in range(0, level_size):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            result.append(level)
        return result        
```
##Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]     
```
##Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)        
```
##Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
    
    
    def isMirror(self, t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)      
```