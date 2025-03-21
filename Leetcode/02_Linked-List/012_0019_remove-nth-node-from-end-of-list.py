# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
# m

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# two scans, no extra DS
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dhead = ListNode(0, head) # dummy head node
        counter = -1 # starts from -1 because of dummy head. returns the len.
        scout = dhead
        while scout:
            scout = scout.next
            counter += 1
        
        target = counter - n # index to delete
        counter = 0 # starts from 0 because our target is scout.next
        scout = dhead
        while counter < target:
            scout = scout.next
            counter += 1
        scout.next = scout.next.next
        return dhead.next

# one scan + stack
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dhead = ListNode(0, head) # dummy head node
        stack = []
        scout = dhead
        while scout:
            stack.append(scout)
            scout = scout.next
        while n >= 0:
            cur = stack.pop()
            n -= 1
        cur.next = cur.next.next
        return dhead.next

# two pointers
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dhead = ListNode(0, head) # dummy head node
        fast = slow = dhead
        for _ in range(n):
            fast = fast.next
        
        while fast.next: # fast will stop at last node
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dhead.next.next