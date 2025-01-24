# Reverse Linked List
# https://neetcode.io/problems/reverse-a-linked-list
# e

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        currentN = head
        prevN = None
        while currentN:
            nextN = currentN.next
            currentN.next = prevN
            prevN = currentN
            currentN = nextN
        return prevN
