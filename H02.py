# uuid_share#  4e746bfe-8d2d-42ca-af59-cb654a86adee  #
# PKUDSA课程上机作业
# 【H2】栈与队列编程作业

# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的*函数体内*编写代码，每个题目的函数后有调用语句用于检验
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守

# ======= 1 中缀表达式求值 =======
# 通过把“中缀转后缀”和“后缀求值”两个算法功能集成在一起（非简单的顺序调用），
# 实现对中缀表达式直接求值，新算法还是从左到右扫描中缀表达式，
# 但同时使用两个栈，一个暂存操作符，一个暂存操作数，来进行求值。

# 创建一个函数，接受参数为一个字符串，即一个中缀表达式，
# 其中每个数字或符号间由一个空格隔开；
# 返回一个浮点数，即求值的结果。（支持 + - * / ^ 五种运算）
#   其中“ / ”定义为真除True DIV，结果是浮点数类型
# 输入样例1：
# ( 2 + 3 ) * 6 + 4 / 2
# 输出样例1：
# 32.0
# 输入样例2：
# 2 ^ 3 + 4 * 5 - 16 / 2
# 输出样例2：
# 20.0
# 输入样例3：
# ( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6
# 输出样例3：
# 1.0


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        out = []
        for i in self.items:
            out.append(str(i))
        return ' | '.join(out)


def do_math(num1, num2, notation):
    num1, num2 = float(num1), float(num2)
    if notation == '+':
        return num1 + num2
    elif notation == '-':
        return num1 - num2
    elif notation == '*':
        return num1 * num2
    elif notation == '/':
        return num1 / num2
    elif notation == '^':
        return num1 ** num2

def calculate(s):

    s = str(s)
    s_cal = Stack()
    s_num = Stack()
    in_lst = s.split()
    pior = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4}

    for i in in_lst:
        if i.isalnum():
            s_num.push(i)
        elif i == '(':
            s_cal.push(i)
        elif i == ')':
            while s_cal.peek() != '(':
                cal_2 = s_num.pop()
                cal_1 = s_num.pop()
                notation = s_cal.pop()
                s_num.push(do_math(cal_1, cal_2, notation))
            s_cal.pop() # 删除对应左括号
        elif i in pior.keys():
            while not s_cal.isEmpty() and pior[i] <= pior[s_cal.peek()]:
                cal_2 = s_num.pop()
                cal_1 = s_num.pop()
                notation = s_cal.pop()
                s_num.push(do_math(cal_1, cal_2, notation))
            s_cal.push(i)
        # print('-'*20)
        # print('num - ||', s_num)
        # print('cal - ||', s_cal)
    
    while not s_cal.isEmpty():
        cal_2 = s_num.pop()
        cal_1 = s_num.pop()
        notation = s_cal.pop()
        s_num.push(do_math(cal_1, cal_2, notation))
    
    return s_num.pop()

# 调用检验
print("======== 1-calculate ========")
print(calculate("( 2 + 3 ) * 6 + 4 / 2"))
print(calculate("2 ^ 3 + 4 * 5 - 16 / 2"))
print(calculate("( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6"))

# ======= 2 基数排序 =======
# 实现一个基数排序算法，用于10进制的正整数从小到大的排序。
#
# 思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
# 第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第三趟放百位，再合并；第四趟放千位，再合并。
# 直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。
#
# 创建一个函数，接受参数为一个列表，为需要排序的一系列正整数，
# 返回排序后的数字列表。
# 输入样例1：
# [1, 2, 4, 3, 5]
# 输出样例1：
# [1, 2, 3, 4, 5]
# 输入样例2：
# [8, 91, 34, 22, 65, 30, 4, 55, 18]
# 输出样例2：
# [4, 8, 18, 22, 30, 34, 55, 65, 91]


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def radix_sort(s):
    # 基数排序参考这里https://www.runoob.com/w3cnote/radix-sort.html
    mainQ = Queue()
    queues = [Queue() for _ in range(10)]
    indicator = 0
    maxnum = 0
    outlst = []

    for i in s:
        mainQ.enqueue(i) # 全部输入 mainQ
        if i > maxnum:
            maxnum = i # 顺便求出最大值，也可以直接用 max()
    
    maxind = len(str(maxnum)) - 1 # 最大数的位数（从 0 起）

    while indicator <= maxind: # 小于最大数字的位数
        while not mainQ.isEmpty(): # 遍历 mainQ
            num = mainQ.dequeue()
            digit = (num // (10 ** indicator)) % 10 # 取当前位数的数字
            queues[digit].enqueue(num) # 放入各个子 queue
        
        for singleQ in queues:
            while not singleQ.isEmpty():
                mainQ.enqueue(singleQ.dequeue()) # 再按顺序汇入 mainQ

        indicator += 1 # 位数+1
    
    while not mainQ.isEmpty():
        outlst.append(mainQ.dequeue())
    
    return outlst

# 调用检验
print("======== 2-radix_sort ========")
print(radix_sort([1, 2, 4, 3, 5]))
print(radix_sort([8, 91, 34, 22, 65, 30, 4, 55, 18]))

# ======= 3 HTML标记匹配 =======
# 实现扩展括号匹配算法，用来检查HTML文档的标记是否匹配。
# HTML标记应该成对、嵌套出现，
# 开标记是<tag>这种形式，闭标记是</tag>这种形式。

# 创建一个函数，接受参数为一个字符串，为一个HTML文档中的内容，
# 返回True或False，表示该字符串中的标记是否匹配。
# 输入样例1：
# <html> <head> <title> Example </title> </head> <body> <h1>Hello, world</h1> </body> </html>
# 输出样例1：
# True
# 输入样例2：
# <html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>
# 输出样例2：
# False


def HTMLMatch(s):
    valid_html = []
    word = ''
    record = False
    s_check = Stack()

    for i in s:
        if i == '<':
            record = True
            continue
        elif i == '>':
            record = False
            valid_html.append(word)
            word = ''
            continue

        if record:
            word += i
    
    for i in valid_html:
        if i[0] != '/':
            s_check.push(i)
        else:
            if i[1:] == s_check.peek():
                s_check.pop()
            else:
                return False
        # print('||', s_check)
    
    return s_check.isEmpty()

# 调用检验
print("======== 3-HTMLMatch ========")
print(
    HTMLMatch(
        "<html> <head> <title>Example</title> </head> <body> <h1>Hello, world</h1> </body> </html>"
    ))
print(
    HTMLMatch(
        "<html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>"
    ))


class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev


# ======== 4 链表实现栈和队列 ========
# 用链表实现ADT Stack与ADT Queue的所有接口

### 从这个作业中，可以部分理解，栈和队列，包括无序表，都是抽象的数据结构类型，他们的核心是 LIFO 和 FIFO
### 而具体的实现，可以用比如 python 中的 list，也可以用链表，等等。
### 链表、python 的 list 等，应该叫某种数据集，他们的区别是物理层面的：在计算机的存储中是如何存储的
### 用 python 的 list 实现的时候，之所以代码短，是因为 python 自己封装了 list 的各种借口，其实背后的代码也不少

class LinkStack():
    def __init__(self):
        self.head = None
    
    def push(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
    
    def pop(self):
        popNode = self.head
        self.head = popNode.next
        return popNode.getData()
    
    def isEmpty(self):
        return not self.head # 这里不可加 getData() 否则如果 data 是 0 或者 flase ，则会错误判断为 Ture
    
    def peek(self):
        return self.head.getData()
    
    def size(self):
        currentNode = self.head
        counter = 0
        while currentNode:
            currentNode = currentNode.next
            counter += 1
        return counter


class LinkQueue():
    def __init__(self):
        self.head = None
    
    def enqueue(self, item):
        newNode = Node(item)
        currentNode = self.head
        if not currentNode:
            self.head = newNode
        else:
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
    
    def dequeue(self):
        dequeueNode = self.head
        self.head = dequeueNode.next
        return dequeueNode.getData()
    
    def isEmpty(self):
        return not self.head
    
    def size(self):
        currentNode = self.head
        counter = 0
        while currentNode:
            currentNode = currentNode.next
            counter += 1
        return counter

# 检验
print("======== 4-Link Stack & Link Queue ========")
s = LinkStack()
q = LinkQueue()
for i in range(10):
    s.push(i)
    q.enqueue(i)
print(s.peek(), q.dequeue())  # 9 0
print(s.pop(), q.size())  # 9 9
while not s.isEmpty():
    s.pop()
print(s.size(), q.isEmpty())  # 0 False

# ======== 5 双链无序表 ========
# 实现双向链表版本的UnorderedList，接口同ADT UnorderedList
# 包含如下方法：isEmpty, add, search, size, remove, append，index，pop，insert, __len__, __getitem__
# 用于列表字符串表示的__str__方法 (注：__str__里不要使用str(), 用repr()代替
# 用于切片的__getitem__方法
# 在节点Node中增加prev变量，引用前一个节点
# 在UnorderedList中增加tail变量与getTail方法，引用列表中最后一个节点
# 选做：DoublyLinkedList(iterable) -> new DoublyLinkedList initialized from iterable's items
# 选做：__eq__, __iter__
class DoublyLinkedList():
    def __init__(self, it = None):
        self.head = None
        self.tail = None
        self.lenth = 0 # 维护一个长度，size可以O(1)
        if it is not None: # 初始化的时候，直接导入一个现有的可迭代对象
            for d in it:
                self.append(d)
    
    def isEmpty(self):
        return not self.head
    
    def add(self, item):
        newNode = Node(item)
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode # 如果是空表，则没有这一步
        else:
            self.tail = newNode # 如果是空表，尾节点设为这个节点
        self.head = newNode
    
    def search(self, item):
        currentNode = self.head
        while currentNode:
            if currentNode.getData() == item:
                return True
            currentNode = currentNode.next
        return False
    
    def size(self):
        return self.lenth # 用上了新维护的lenth属性

    __len__ = size # 定义魔术方法 __len__
    
    def remove(self, item):
        currentNode = self.head
        while currentNode:
            if currentNode.getData() == item:
                currentNode.prev.next = currentNode.next
                currentNode.next.prev = currentNode.prev
                return True # 删除成功返回 true，反之返回 false
            currentNode = currentNode.next
        return False
    
    # 这是还没有加入尾结点时的代码：
    # def append(self, item):
    #     newNode = Node(item)
    #     if not self.head:
    #         self.add(item)
    #     else:
    #         currentNode = self.head
    #         while currentNode.next:
    #             currentNode = currentNode.next
    #         currentNode.next = newNode
    #         newNode.prev = currentNode
    
    # 加入尾结点：
    def append(self, item):
        newNode = Node(item)
        newNode.prev = self.tail
        if self.tail:
            self.tail.next = newNode # 非空表
        else:
            self.head = newNode # 空表
        self.tail = newNode
    
    def index(self, item):
        currentNode = self.head
        counter = 0
        while currentNode:
            if currentNode.getData() == item:
                return counter
            currentNode = currentNode.next
            counter += 1
        return None
    
    def pop(self, pos = -1):
        currentNode = self.head
        counter = 0
        if pos == 0:
            self.head = currentNode.next
            currentNode.next.prev = None
            return currentNode.getData()
        elif pos == -1:
            currentNode = self.tail # 直接等于尾结点
            self.tail = currentNode.prev
            currentNode.prev.next = None
            return currentNode.getData()
        else:
            while counter != pos:
                currentNode = currentNode.next
                counter += 1
            currentNode.next.prev = currentNode.prev
            currentNode.prev.next = currentNode.next
            return currentNode.getData()
    
    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        elif pos == self.size() - 1:
            self.append(item)
        else:
            newNode = Node(item)
            currentNode = self.head
            counter = 0
            while counter != pos:
                currentNode = currentNode.next
                counter += 1
            newNode.next = currentNode
            newNode.prev = currentNode.prev
            currentNode.prev.next = newNode
            currentNode.prev = newNode
    
    def getTail(self):
        return self.tail
    
    def __getitem__(self, index):
        counter = 0
        if isinstance(index, slice):
            start = 0 if index.start is None else index.start # 严谨的写法，余同
            stop = self.size() if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            # start = index.start or 0
            # stop = index.stop or self.size()
            # step = index.step or 1
            currentNode = self.head if step > 0 else self.tail # 考虑负数步长
            counter = 0 if step > 0 else self.size() # 考虑负数步长
            stepCounter = 0
            outLst = DoublyLinkedList() # 切片对象也应该是双链表
            if step > 0:
                while counter < start: # 遍历直到start
                    currentNode = currentNode.getNext()
                    counter += 1
                while counter < stop: # 只能用小于，以防 step 过大
                    # currentNode = currentNode.next # 其实区别不大，换下面写法也行
                    # counter += 1
                    # stepCounter += 1
                    # if stepCounter % step == 0:
                    #     outLst.append(currentNode.getData())
                    outLst.append(currentNode.getData())
                    stepCounter = step
                    while currentNode is not None and stepCounter > 0:
                        currentNode = currentNode.getNext()
                        stepCounter -= 1
                    counter += step
            elif step < 0:
                while counter > stop:
                    currentNode = currentNode.getPrev()
                    counter -= 1
                while counter > start:
                    outLst.append(currentNode.getData())
                    stepCounter = -step # stepcounter 取正
                    while currentNode is not None and stepCounter > 0:
                        currentNode = currentNode.getPrev()
                        stepCounter -= 1
                    counter += step
            return outLst
        elif isinstance(index, int): # 不能直接 else
            currentNode = self.head
            while counter != index:
                currentNode = currentNode.next
                counter += 1
            if currentNode is not None:
                return currentNode.getData()
            else:
                raise StopIteration # 要判断是否超出边界，终止迭代
    
    def __str__(self):
        outLst = []
        currentNode = self.head
        while currentNode:
            outLst.append(repr(currentNode.getData()))
            currentNode = currentNode.next
        return '[ ' + ' |<->| '.join(outLst) + ' ]'
    
    def __iter__(self): # 捕捉for 循环时，调用一次
        self.currentNode = self.head
        return self
    
    def __next__(self): # for循环捕捉 stopiter 异常之前，都是调用这个 next
        if self.currentNode:
            data = self.currentNode.getData()
            self.currentNode = self.currentNode.next
            return data
        else:
            raise StopIteration

    def __eq__(self, other):
        if isinstance(other, type(self)):
            for i, j in zip(self, other): # 用 zip 把两个链表中的对象依次取出来配对，同时也利用了上面写的迭代器特性。
                if i != j:
                    return False
            return self.size() == other.size()
        else:
            return False
            


# 检验
print("======== 5-DoublyLinkedList ========")
mylist = DoublyLinkedList()
for i in range(0, 20, 2):
    mylist.append(i)
mylist.add(3)
mylist.remove(6)
print(mylist.getTail().getPrev().getData())  # 16
print(mylist.isEmpty())  # False
print(mylist.search(5))  # False
print(mylist.size())  # 10
print(mylist.index(2))  # 2
print(mylist.pop())  # 18
print(mylist.pop(2))  # 2
print(mylist)  # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))  # 9
print(mylist[4])  # 8
print(mylist[3:8:2])  # ['10', 10, 14]
iterlist = DoublyLinkedList()
for i in mylist:
    iterlist.append(i)
print(iterlist)
print(iterlist == mylist)