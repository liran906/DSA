import sys, random
sys.path.append('.')
from pythonds.basic.queue import Queue

class Printer:
    def __init__(self, speed):
        self.isBusy = False
        self.speed = speed
        self.printTime = 0
        self.waitDict = {}
    
    def print(self, task, globalTime):
        self.printTime = task.pages * (60 / self.speed)
        self.isBusy = True
        self.waitDict[task.id] = globalTime - task.startTime # 记录等待时长
    
    def tick(self, queue, globalTime):
        self.printTime -= 1 # 打印耗时 -1
        if self.printTime <= 0:
            if queue.isEmpty():
                self.isBusy = False
            else:
                toPrint = queue.dequeue() # 开始下一个打印任务
                self.print(toPrint, globalTime)

class Task:
    def __init__(self, id, globalTime):
        self.id = id
        self.pages = random.randint(1,20)
        self.startTime = globalTime

def main(speed, totalTime = 3600, genRate = 180):
    taskQ = Queue()
    printer = Printer(speed)
    taskID = 0

    for time in range(totalTime):
        if random.randint(0, genRate - 1) == 0:
            taskQ.enqueue(Task(taskID, time))
            taskID += 1
        printer.tick(taskQ, time)
    
    finished = taskID if not printer.isBusy else taskID - taskQ.size() - 1
    waitTime = 0
    for i in printer.waitDict.values():
        waitTime += i
    aveWaitTime = waitTime / len(printer.waitDict)
    finish = finished / taskID # 完成率
    
    # print(
    #     f'共生成{taskID}个任务，打印完成{finished}个任务，平均等待{aveWaitTime:.2f}秒'
    # )

    # for i in printer.waitDict:
    #     print(f'任务ID：{i}, 打印等待{printer.waitDict[i]}秒')

    return aveWaitTime, finish

# 多次模拟输出平均结果：
repeat = 10
speed = 6

for test in [5,6,8,10,12,15,20,30,45,60]:
    att = 0
    attper = 0
    for i in range(repeat):
        result, percentage = main(test)
        att += result
        attper += percentage
    print(f'打印速度为每分钟{test}页，重复模拟{repeat}次，平均完成率为{(attper/repeat*100):.1f}%，平均等待时长为{att/repeat:.1f}秒')