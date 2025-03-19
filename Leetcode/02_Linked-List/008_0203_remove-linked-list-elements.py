# https://leetcode.cn/problems/remove-linked-list-elements/
# e

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        # 如果头节点就是要删的
        while head and head.val == val:
            head = head.next
        
        # 如果给空链表，或者被上一步head删的只剩下空链表
        # if not head:
        #     return head
        
        current = head
        # while current 判断是否是空链表
        while current and current.next:
            current, parent = current.next, current
            if current.val == val:
                parent.next = current.next
                current = parent
        return head
    
    # def del_child(self, node):
    #     if node.next:
    #         new_child = node.next.next
    #         node.next = new_child

    # 方法 2 设置一个虚拟头节点，这样不用专门的逻辑来处理头节点
    def removeElements(self, head, val):
        dhead = ListNode(next=head)
        current = dhead
        while current.next: # 其实不需要parent 变量
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dhead.next
    
    # 方法 3 递归
    def removeElements(self, head, val):
        if head is None:
            return head
        
        head.next = self.removeElements(head.next, val)

        if head.val == val:
            return head.next
        
        return head