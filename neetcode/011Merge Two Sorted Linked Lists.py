# Merge Two Sorted Linked Lists
# https://neetcode.io/problems/merge-two-sorted-linked-lists
# e

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None
        head = None
        while list1 and list2:
            if list1.val < list2.val:
                newnode = ListNode(list1.val)
                list1 = list1.next
            else:
                newnode = ListNode(list2.val)
                list2 = list2.next

            if not head:
                newlist = newnode
                head = newlist
            else:
                newlist.next = newnode
                newlist = newlist.next
            
        remainder = list1 if list1 else list2
        while remainder:
            newnode = ListNode(remainder.val)
            if not head:
                newlist = newnode
                head = newlist
            else:
                newlist.next = newnode
                newlist = newlist.next
            remainder = remainder.next
        return head

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = nlist = ListNode()

        # This will mess up the previous linkedlists, but whatever.
        while list1 and list2:
            if list1.val < list2.val:
                nlist.next = list1
                list1 = list1.next
            else:
                nlist.next = list2
                list2 = list2.next
            nlist = nlist.next
        
        # Don't need to go through the rest. Just point towards it.
        nlist.next = list1 if list1 else list2
        return head.next

# Recrusion
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2