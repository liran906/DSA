class Queue(list):
    enqueue = list.append
    dequeue = lambda self: self.pop(0)
    isEmpty = lambda self: len(self) == 0
    peek = lambda self: self[0]
    size = list.__len__

def func(mylist):
    mainQ = Queue()
    queues = [Queue() for i in range(10)]
    indicator = 0
    maxnum = max(mylist)
    maxind = len(str(maxnum))
    output = []

    for i in mylist:
        mainQ.enqueue(i)
    
    while indicator <= maxind:
        while not mainQ.isEmpty():
            currentNum = mainQ.dequeue()
            digit = (currentNum // (10 ** indicator)) % 10
            queues[digit].enqueue(currentNum)
        for q in queues:
            while not q.isEmpty():
                mainQ.enqueue(q.dequeue())
        indicator += 1

    while not mainQ.isEmpty():
        output.append(mainQ.dequeue())
    return output
    
mylist = eval(input())
print(func(mylist))