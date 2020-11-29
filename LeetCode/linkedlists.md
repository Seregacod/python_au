# Linkedlists

+ [Design Linked List](Design Linked List)

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