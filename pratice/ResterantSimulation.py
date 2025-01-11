import sys
sys.path.append('.')
from pythonds.basic.queue import Queue
from random import randint

class Customer:
    def __init__(self, id, gTime):
        self.num = randint(1, 4)
        if self.num == 1:
            self.plate = randint(1, 3)
        elif self.num == 2:
            self.plate = randint(2, 5)
        elif self.num == 3:
            self.plate = randint(3, 6)
        else:
            self.plate = randint(4, 7)

        self.enterTime = gTime
        self.diningTime = 8 + 4 * self.num + 8 * self.plate
        self.spentTime = 0
        self.finish = False
        self.seated = False
        self.id = id
        self.dishes = [False] * self.plate
    
    def dine(self, waitingTime):
        self.diningTime += 1
        if self.diningTime == self.time: # 结束用餐
            self.finish = True
            return waitingTime, self.diningTime
    
    def order(self):
        return self.id, self.plate
    
    def getID(self):
        return self.id
    
    def getPlate(self):
        return self.plate

class Task:
    def __init__(self, customer):
        self.plateNum = customer.getPlate()
        self.id = customer.getID()
        self.isDone = False
    
    def initPlateTime(self):
        return randint(2, 4)
    
    def getPlateNum(self):
        return self.plateNum
    
    def setPlateNum(self, num):
        self.plateNum = num

    def getID(self):
        return self.id

class Chief:
    def __init__(self):
        self.salory = 8000
        self.busy = False
    
    def cook(self, task):
        self.busy = True
    
    def tick(self, taskQ):
        if not self.isBusy() and not taskQ.isEmpty():
            self.cookTask = taskQ.dequeue()
            self.timeRemain = self.cookTask.initPlateTime()
            self.cookTask.setPlateNum(self.cookTask.getPlateNum() - 1)
            if self.cookTask.getPlateNum() > 0:
                taskQ.enqueue(self.cookTask)
            self.cook(self.cookTask)
        elif self.isBusy():
            if self.timeRemain > 0:
                self.timeRemain -= 1
            else:
                self.busy = False
                return self.cookTask.getID()


    def isBusy(self):
        return self.isBusy

class Waiter:
    pass

class Table:
    def __init__(self, id):
        self.occupy = False
        self.occupyNum = 0
        self.occupyID = None
        self.tableID = id
    
    def isOccupied(self):
        return self.occupy
    
    def occupy(self, customer):
        if not self.occupy:
            self.occupy = True
            self.occupyID = customer.getID()
    
    def getID(self):
        return self.tableID
    
    def setOID(self, id):
        self.occupyID = id

def simulate(totaltime, fund, chiefNum, waiterNum):
    salory = 8000 * chiefNum + 5500 * waiterNum
    tableNum = (fund - salory - 20000) / 2000
    chiefs = [Chief() for _ in range(len(chiefNum))]
    waiters = [Waiter() for _ in range(len(waiterNum))]
    tables = [Table() for _ in range(len(tableNum))]
    taskQueue = Queue()
    customerQueue = Queue()
    cusID = 0

    for time in totaltime:
        # 判断是否生成顾客
        isCustomer = randint(0,5)
        if isCustomer == 0:
            customer = Customer(cusID, time)
            customerQueue.enqueue(customer)
            cusID += 1
        
        # 判断是否能上桌
        if not customerQueue.isEmpty():
            for table in tables:
                if not table.isOccupied():
                    currentCustomer = customerQueue.dequeue()
                    table.setOID(currentCustomer.getID()) # 桌子编号
                    currentTask = Task(currentCustomer)
                    taskQueue.enqueue(currentTask)

        # execute tick
        for chief in chiefs:
            finishID = chief.tick(taskQueue)
            if finishID is not None:
                pass

