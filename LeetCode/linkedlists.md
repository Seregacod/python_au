# Linkedlists

+ [Design Linked List](#Design Linked List)
+ [Reverse Linked Lists](#Reverse Linked Lists)
+ [Middle of the Linked List](#Middle of the Linked List)
+ [Palindrome Linked List](#Palindrome Linked List)
+ [Merge Two Sorted Lists](#Merge Two Sorted Lists)
+ [Remove Nth Node From End of List](#Remove Nth Node From End of List)
+ [Linked List Cycle II](#Linked List Cycle II)
+ [Linked List Cycle](#Linked List Cycle)
+ [Reorder List](#Reorder List)
+ [Intersection of Two Linked Lists](#Intersection of Two Linked Lists)
+ [Sort List](#Sort List)

## Design Linked List
https://leetcode.com/problems/design-linked-list/
```python
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        i = 0
        node = self.head

        while node:
            if index == i:
                return node.get("value")
            node = node.get("next")
            i = i + 1

        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        new_node = { "value": val, "next": self.head, "prev": None }
        if self.head:
            self.head.update({ "prev": new_node })
        self.head = new_node
        self.length = self.length + 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """


        node = self.head
        while node.get("next"):
            node = node.get("next")
        new_node = { "value": val, "prev": node, "next": None }
        node.update({ "next": new_node })
        self.length = self.length + 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            return self.addAtHead(val)
        if index == self.length:
            return self.addAtTail(val)

        i = 0
        node = self.head
        while node:
            # find correct position
            if index == i:
                new_node = { "value": val, "next": node, "prev": node.get("prev") }
                node.get("prev").update({ "next": new_node })
                node.update({ "prev": new_node })
                self.length = self.length + 1
                return None
            node = node.get("next")
            i = i + 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        i = 0
        node = self.head
        while node:
            if index == i:
                next_node = node.get("next")
                prev_node = node.get("prev")
                if index == 0:
                    self.head = next_node
                if next_node:
                    next_node.update({ "prev": prev_node })
                if prev_node:
                    prev_node.update({ "next": next_node })
                self.length = self.length - 1
                return None
            node = node.get("next")
            i = i + 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```
##Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p 
```
##Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) / 2]        
```
##Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reversed_head = self.reverse(head)

        while (head != None and reversed_head != None):

            if (head.val != reversed_head.val):
                return False
            
            head = head.next
            reversed_head = reversed_head.next
        
        return True
    
    def reverse(self, head):        
        prev = None
                
        dummy = ListNode(0)
        dummy.next = head
        current = head
                
        while (current != None):
            new = ListNode(current.val)
            new.next = prev
            prev = new
            current = current.next
        
        head = dummy.next
        
        return prev    
```
##Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2      
```
##Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 1
        cur = p = head
        while cur.next:
            size += 1
            cur = cur.next
            if size > n + 1:
                p = p.next
        if size == n:
            return head.next
        else:
            p.next = p.next.next
            return head        
```
##Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = b = head

        while a and a.next:
            a = a.next.next
            b = b.next
            if a == b:
                seek = head
                while seek != b:
                    b = b.next
                    seek = seek.next
                return b    
```
##Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False        
        b, a = head, head.next
        while b != a:
            if not a or not a.next: return False
            b, a = b.next, a.next.next
        return True        
``` python
##Reorder List
https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None: return
        
        b, a = head, head
        while a != None and a.next != None:
            b = b.next
            a = a.next.next
        
        p, c = None, b
        while c != None:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
        
        n1, n2 = head, p
        while n2.next != None:
            tmp = n1.next
            n1.next = n2
            n1 = tmp
            
            tmp = n2.next
            n2.next = n1
            n2 = tmp      
```       
##Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None

        A_point = headA
        B_point = headB

        while A_point != B_point:
            A_point = headB if A_point == None else A_point.next
            B_point = headA if B_point == None else B_point.next

        return A_point        
```
##Sort List
https://leetcode.com/problems/sort-list/
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        def getSize(head):
            counter = 0
            while head:
                counter +=1
                head = head.next
            return counter
        
        def split(head, size):
            for i in range(size-1): 
                if not head: 
                    break 
                head = head.next

            if not head: return None
            next_start, head.next = head.next, None 
            
            return next_start
        
        def merge(l1, l2, dummy_start):
            curr = dummy_start
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next
            
            curr.next = l1 if l1 else l2
            while curr.next: curr = curr.next 
            return curr  

        total_length = getSize(head)
        dummy = ListNode(0)
        dummy.next = head
        start, dummy_start, size = None, None, 1
        
        while size < total_length:
            dummy_start = dummy
            start = dummy.next 
            while start:
                left = start
                right = split(left, size) 
                start = split(right, size) 
                dummy_start = merge(left, right, dummy_start)  
            size *= 2
        return dummy.next    
```