# https://leetcode.cn/problems/reverse-linked-list/
# e

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def reverseList(self, head):
#         if not head:
#             return
#         p_node = None
#         c_node = head
#         n_node = head.next
#         while n_node:
#             c_node.next = p_node
#             p_node = c_node
#             c_node = n_node
#             n_node = n_node.next
#         c_node.next = p_node
#         return c_node

class Solution(object):
    def reverseList(self, head):
        p_node = None
        c_node = head
        while c_node:
            tmp = c_node.next
            c_node.next = p_node
            p_node = c_node
            c_node = tmp
        return p_node
    
# recursive
class Solution(object):
    def reverseList(self, head):
        return self.reverse(head, None)

    def reverse(self, curr, prev):
        if curr == None:
            return prev
        next = curr.next
        curr.next = prev
        return self.reverse(next, curr)