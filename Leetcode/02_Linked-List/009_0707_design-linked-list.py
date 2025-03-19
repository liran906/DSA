# https://leetcode.com/problems/design-linked-list
# m

class Node(object):
    def __init__(self, val=0, next=None, prev=None):
        self.__dict__.update(val=val, next=next, prev=prev)

class MyLinkedList(object):
    def __init__(self, head=None, tail=None):
        self.__dict__.update(head=head, tail=tail, size=0)
    
    def _get(self, index):
        if not 0 <= index < self.size:
            return None
        
        if index == 0:
            return self.head
        elif index == self.size - 1:
            return self.tail
        
        # 从头部遍历到 index
        elif index <= self.size // 2:
            i = 1
            current = self.head.next
            while i < index:
                current = current.next
                i += 1
        
        # 从尾部遍历到 index
        elif self.size // 2 < index < self.size - 1:
            i = self.size - 2
            current = self.tail.prev
            while i > index:
                current = current.prev
                i -= 1
        return current

    def get(self, index):
        node = self._get(index)
        if not node:
            return -1
        return node.val
    
    def addAtHead(self, val):
        new_node = Node(val)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        else: # 没有头节点，也就是空链表，也就没有尾节点
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
        else: # 同上
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            current = self._get(index)
            if current:
                new_node = Node(val)
                self.size += 1

                # 四个指针调整
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node

    def deleteAtIndex(self, index):
        current = self._get(index)
        if current:
            if current == self.head:
                self.head = self.head.next
                current.next = None
            if current == self.tail:
                self.tail = self.tail.prev
                current.prev = None
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            self.size -= 1

m = MyLinkedList()
m.addAtHead(1)
m.addAtTail(7)
m.addAtTail(1)
m.addAtTail(8)
m.addAtHead(8)
m.addAtIndex(5,2)
m.addAtTail(7)
print(m.get(2))