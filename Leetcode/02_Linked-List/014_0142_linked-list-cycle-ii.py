# https://leetcode.cn/problems/linked-list-cycle-ii/
# m

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        hashtable = set()
        cur = head
        while cur:
            if cur in hashtable:
                return cur
            hashtable.add(cur)
            cur = cur.next
        return None

# 双指针，解释看
# https://leetcode.cn/problems/linked-list-cycle-ii/solutions/12616/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/

class Solution(object):
    def detectCycle(self, head):
        fast = slow = head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast