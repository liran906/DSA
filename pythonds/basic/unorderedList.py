import sys
sys.path.append('.')
from pythonds.basic.node import Node

class Unorderedlist:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        lst = []
        current = self.head
        while current:
            lst.append(current.getData())
            current = current.next
        return ' --- '.join(lst)
    
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
    
    def remove(self, item = None): # 只删除遇到的第一个，如果删了返回 ture 否则返回false
        if not self.head: # 是空表
            return False
        if self.head.getData() == item: # 是第一个节点
            self.head = self.head.next
            return True
        if not item: # item为空，则直接删除第一个节点
            self.head = self.head.next
            return True
        else:
            prev = None
            current = self.head

            while current:
                if current.getData() == item:
                    prev.next = current.next
                    return True
                prev = current
                current = current.next
            return False
    
    def search(self, item):
        current = self.head
        while current:
            if current.getData() == item:
                return True
            current = current.next
        return False
    
    def isEmpty(self):
        return not self.head
    
    def size(self):
        current = self.head
        counter = 0

        while current:
            current = current.next
            counter += 1
        return counter
    
    def append(self, item):
        newNode = Node(item)
        if not self.head: # 空表
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
    
    def index(self, item):
        current = self.head
        counter = 0

        while current:
            if current.getData() == item:
                return counter
            current = current.next
            counter += 1
        return None # 没找到则返回none
    
    def insert(self, pos, item):
        if pos == 0: # 头插
            self.add(item)
            return
        
        newNode = Node(item)
        current = self.head
        counter = 0

        while counter < pos - 1:
            current = current.next
            counter += 1
        
        newNode.next = current.next
        current.next = newNode
    
    def pop(self, pos = None):
        if not self.head: # 空表
            return
        elif not self.head.next: # 只有一个节点
            v = self.head.getData()
            self.head = None
            return v
        elif pos == 1:
            v = self.head.getData()
            self.head = self.head.next
            return v
        else:
            prev = None
            current = self.head
            counter = 1
            while counter != pos and current.next:
                prev = current
                current = current.next
                counter += 1
            prev.next = current.next
            return current.getData()

if __name__ == '__main__':
    ll = Unorderedlist()
    for i in range(9,-1,-1):
        ll.add(str(i))
    
    print(ll.size())
    print(ll)
    ll.pop()
    print(ll)
    print(ll.pop(1))
    print(ll)
    ll.remove('4')
    print(ll)
    ll.remove()
    print(ll)
    print(ll.index('5'))
    print(ll.search('8'))