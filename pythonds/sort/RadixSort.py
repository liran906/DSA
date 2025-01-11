import sys
sys.path.append('.')
from pythonds.basic.linkedQueue import LinkedQueue

def radixSort(s):
    # 基数排序参考这里https://www.runoob.com/w3cnote/radix-sort.html
    mainQ = LinkedQueue()
    queues = [LinkedQueue() for _ in range(10)]
    indicator = 0
    maxnum = max(s)
    maxind = len(str(maxnum)) - 1 # 最大数的位数（从 0 起）
    outlst = []

    for i in s:
        mainQ.enqueue(i) # 全部输入 mainQ

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
if __name__ == '__main__':
    print(radixSort([1, 2, 4, 3, 5]))
    print(radixSort([8, 91, 34, 22,222,3215,222,222,22,30, 65, 30, 4, 55, 18]))