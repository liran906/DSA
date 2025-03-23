# https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/
# e

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two stacks - space O(n+m)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA = headA
        curB = headB
        stackA = []
        stackB = []
        while curA:
            stackA.append(curA)
            curA = curA.next
        while curB:
            stackB.append(curB)
            curB = curB.next
        
        res = None
        while stackA and stackB and stackA[-1] == stackB[-1]:
            res = stackA[-1]
            stackA.pop()
            stackB.pop()
        return res

# hash table - space O(n)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        curA = headA
        curB = headB
        htable = set()

        while curA:
            htable.add(curA)
            curA = curA.next
        
        while curB:
            if curB in htable:
                return curB
            curB = curB.next
        return None

# two pointers - space O(1)
'''
如链表A+链表B=链表C1
链表B+链表A=链表C2
A -> a1 a2 c1 c2 c3
B -> b1 b2 b3 c1 c2 c3
C1 -> a1 a2 c1 c2 c3 b1 b2 b3 c1 c2 c3
C2 -> b1 b2 b3 c1 c2 c3 a1 a2 c1 c2 c3
此时C1和C2的长度一定相同。
而C1和C2的结尾就一定是相交的链表。
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        curA = headA
        curB = headB
        switched = 0

        while curA and curB:
            if curA == curB:
                return curA
            
            curA = curA.next
            curB = curB.next

            if not curA and switched < 2:
                curA = headB
                switched += 1
            if not curB and switched < 2:
                curB = headA
                switched += 1
        
        return None