# OJ结果是错的，但我不明白哪里错了

class Queue(list):
    enqueue = list.append
    dequeue = lambda self: self.pop(0)
    isEmpty = lambda self: len(self) == 0
    peek = lambda self: self[0]
    size = list.__len__

def func(mylist):
    q = Queue()
    output = []
    for i in mylist:
        q.enqueue(i)
        cmin = i - 10000
        while q.peek() < cmin:
            q.dequeue()
        output.append(q.size())
    return output

def func(mylist):
    output = []
    for _, i in enumerate(mylist):
        cmin = i - 10000
        count = 1
        for j in range(_):
            if mylist[j] >= cmin:
                count += 1
        output.append(count)
    return output
    
# mylist = eval(input())
mylist = [0,10,100,1000,10000,10010,20000,100000]
print(func(mylist))

mylist = [1, 100, 10500, 20500]
print(func(mylist)) # 输出: [1, 2, 1, 2]
mylist = [1000, 2000, 3000, 4000, 5000]
print(func(mylist)) # 输出: [1, 2, 3, 4, 5]
mylist = [0, 20000, 40000, 60000]
print(func(mylist))
# 输出: [1, 1, 1, 1]