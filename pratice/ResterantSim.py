import sys
sys.path.append('.')
from pythonds.basic.queue import Queue
from random import randint

class Customer:
    def __init__(self, id, gTime):
        self.num = randint(1, 4)
        self.id = id
        self.enterTime = gTime
        self.sTime = None
        self.endTime = None
        self.eatTime = None
        self.diningTime = 15 * self.num
        self.done = False

    def setPlate(self, plate):
        self.plates = [False] * plate
    
    def serve(self, gTime):
        pnum = len(self.plates)
        for i in range(pnum - 1): # 提前一个盘子就得进入 else 了
            if self.plates[i] == False:
                self.plates[i] = True
                if i == 0:
                    self.table.setEatTime(gTime)
                break
        else:
            if pnum == 1: # 要考虑盘子数为 1 的时，上面一减成 0 了
                self.table.setEatTime(gTime)
            self.plates[-1] = True
            self.done = True
            self.table.setAllServed(gTime)
            self.endTime = gTime

    def getID(self):
        return self.id
    
    def getNum(self):
        return self.num
    
    def sitTime(self, gTime):
        self.sTime = gTime
    
    def setTable(self, table):
        self.table = table
    
    def getTime(self):
        return self.enterTime, self.sTime, self.endTime

class Task:
    def __init__(self, customer):
        self.cus = customer
        self.done = False

        num = self.cus.getNum()
        if num == 1:
            plate = randint(1, 3)
        elif num == 2:
            plate = randint(2, 5)
        elif num == 3:
            plate = randint(3, 6)
        elif num == 4:
            plate = randint(4, 7)
        self.cus.setPlate(plate) # 传递一个数量给 customer
        self.plate = [Plate(self.cus)] * plate # 每个 plate 烹饪时长组成的 list

    def getCustomer(self):
        return self.cus
    
    def getPlate(self):
        if len(self.plate) == 1:
            self.done = True
        return self.plate.pop()
    
    def isDone(self):
        return self.done

class Plate:
    def __init__(self, customer):
        self.cus = customer
        self.done = False
        self.doneTime = randint(2, 4)
    
    def getDTime(self):
        return self.doneTime
    
    def ticDTime(self):
        self.doneTime -= 1

    def setDone(self, gTime):
        if self.doneTime <= 0:
            self.done = True
            self.cus.serve(gTime)

class Chief:
    def __init__(self):
        self.salory = 8000
        self.busy = False
        self.plate = None
    
    def cook(self, plate):
        self.busy = True
        self.plate = plate

    def isBusy(self):
        return self.busy
    
    def tick(self, gTime):
        if self.plate:
            if self.plate.getDTime() > 0:
                self.plate.ticDTime()
            else:
                self.plate.setDone(gTime)
                self.busy = False
                self.plate = None

class Table:
    def __init__(self):
        self.cus = None
        self.occu = False
        self.eatTime = None
        self.allSTime = None
        self.allServed = False
        self.count = 0
    
    def isOccupied(self):
        return self.occu
    
    def occupy(self, customer):
        self.cus = customer
        self.diningTime = 15 * self.cus.num
        self.occu = True
    
    def setEatTime(self, time):
        self.eatTime = time
    
    def setAllServed(self, time):
        self.allSTime = time
        self.allServed = True
    
    def unoccupy(self):
        self.cus = None
        self.occu = False
        self.eatTime = None
        self.allSTime = None
        self.allServed = False
    
    def tick(self, gTime):
        if (self.occu and self.allServed and 
            (gTime - self.eatTime > self.diningTime) and 
            (gTime - self.allSTime > 10)):
            self.count += 1
            self.unoccupy()

def simulate(totaltime, fund, chiefNum, waiterNum):
    salory = 8000 * chiefNum + 5500 * waiterNum
    tableNum = (fund - salory - 20000) / 2000
    chiefs = [Chief() for _ in range(chiefNum)]
    # waiters = [Waiter() for _ in range(len(waiterNum))]
    tables = [Table() for _ in range(int(tableNum))]
    taskQueue = Queue()
    customerQueue = Queue()
    allCustomers = []
    cusID = 0

    for time in range(totaltime):
        # 判断是否生成顾客
        isCustomer = randint(0,6)
        if isCustomer == 0:
            customer = Customer(cusID, time)
            customerQueue.enqueue(customer)
            allCustomers.append(customer)
            cusID += 1
        
        # 判断是否上桌
        for table in tables:
            table.tick(time)
            if not customerQueue.isEmpty():
                if not table.isOccupied():
                    currentCustomer = customerQueue.dequeue() # 出列
                    currentCustomer.sitTime(time) # 计时
                    currentCustomer.setTable(table) # table对象 给cus对象
                    table.occupy(currentCustomer) # 桌子标记被占
                    currentTask0 = Task(currentCustomer)
                    taskQueue.enqueue(currentTask0) # 生成任务并入队
                    break

        # 给空闲厨师分配任务
        for chief in chiefs:
            chief.tick(time) # 执行任务
            if (not chief.isBusy()) and (not taskQueue.isEmpty()): # 分配新任务
                currentTask = taskQueue.dequeue()
                currentPlate = currentTask.getPlate()
                chief.cook(currentPlate)
                if not currentTask.isDone():
                    taskQueue.enqueue(currentTask)

    # 统计时间
    unsit = 0 # 人数
    undone = 0 # 人数
    queueTime = 0
    eatTime = 0
    num = len(allCustomers)
    for cus in allCustomers:
        et, st, dt = cus.getTime()
        if st is None:
            unsit += 1
            queueTime += totaltime - et
        elif dt is None:
            undone += 1
            queueTime += st - et
            eatTime += totaltime - st
        else:
            queueTime += st - et
            eatTime += dt - st
    aveqt = queueTime / num
    avedt = eatTime / (num - unsit)
    print(f'Total {fund} envestment, {chiefNum} chiefs, {int(tableNum)} tables.')
    print(f'Total {num} customers, {unsit} did not have seats, {undone} did not finish their meals.')
    print(f'Average queuing time is {aveqt:.2f} minutes, average waiting time till meal is all served is {avedt:.2f} minutes.')

simulate(300, 58000, 2, 2)