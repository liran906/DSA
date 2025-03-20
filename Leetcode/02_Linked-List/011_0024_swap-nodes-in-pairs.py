# https://leetcode.cn/problems/swap-nodes-in-pairs/
# m

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        if head:
            ll1 = head # linklist1: 1-3-5...
            ll2 = head.next # linklist2: 2-4-6...
            if ll2:
                head = ll2 # new head
            while ll2: # while 2+ nodes
                tmp1 = ll2.next # temp1: linklist1.next
                if tmp1: # 3 or 4+ nodes left
                    tmp2 = tmp1.next # temp2: linklist2.next
                    ll2.next = ll1
                    # if only 3 nodes left: ll1.next = tmp1
                    # else (4 nodes left) : ll1.next = tmp2
                    ll1.next = tmp1 if (not tmp2 and tmp1) else tmp2 
                    ll1 = tmp1
                    ll2 = tmp2
                else: # 2 nodes left
                    ll2.next = ll1
                    ll1.next = None
            ll1.next = None # 1 node left
            return head

# Use Stack
# https://leetcode.cn/problems/swap-nodes-in-pairs/solutions/41485/dong-hua-yan-shi-24-liang-liang-jiao-huan-lian-bia/
class Solution(object):
    def swapPairs(self, head):
        if not (head and head.next):
            return head
        stack = []
        curr = head
        head = None
        count = 0
        while curr:
            count += 1
            stack.append(curr)
            curr = curr.next
            if count % 2 == 0:
                while stack:
                    if not head: # for the first time
                        head = stack.pop()
                        new_link = head
                    new_link.next = stack.pop()
                    new_link = new_link.next
        if stack: # empty the stack after loop (can remain 1 node)
            new_link.next = stack.pop()
            new_link = new_link.next
        new_link.next = None # last node
        return head

# iter with dummy as head
class Solution(object):
    def swapPairs(self, head):
        if not (head and head.next):
            return head
        
        dhead = ListNode(0, head)
        cur = head
        tmp = dhead
        while cur and cur.next:
            nxt = cur.next
            tmp.next = nxt
            cur.next = nxt.next
            nxt.next = cur
            tmp = cur
            cur = cur.next
        return dhead.next




# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n1.next = n2
# n2.next = n3
# n3.next = n4

# s = Solution()
# s1 = s.swapPairs(n1)
# while s1:
#     print(s1.val)
#     s1 = s1.next