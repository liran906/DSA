# Linked List Cycle Detection
# https://neetcode.io/problems/linked-list-cycle-detection
# e

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        p1 = p2 = head
        count = 0
        while p1:
            p1 = p1.next
            p2 = p2.next if count % 2 == 1  else p2
            count += 1
            if p1 == p2:
                return True
        return False