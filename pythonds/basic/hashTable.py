class HashTable:
    def __init__(self, size=11, load_factor=0.65):
        self.size = self.nextprime(size - 1)
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.load_factor = load_factor
        self.lenth = 0
        self.collisions = 0
    
    def hashfunction(self, key):
        return key % self.size
    
    def rehash(self, oldhash):
        return (oldhash + 1) % self.size
    
    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] is not None:
            self.collisions += 1
            while self.slots[hashvalue] is not None:
                if self.slots[hashvalue] == key:  # 如果找到相同的 key，直接更新值并返回
                    self.data[hashvalue] = data
                    return
                hashvalue = self.rehash(hashvalue)

        # 找到空槽，插入新值
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
        self.lenth += 1

        # 动态扩展检查
        if self.lenth / self.size >= self.load_factor:
            self.resize()

    # 写法不够简洁：
    # def put(self, key, data):
    #     hashvalue = self.hashfunction(key)
    #     if self.slots[hashvalue] == None:
    #         self.slots[hashvalue] = key
    #         self.data[hashvalue] = data
    #         self.lenth += 1
    #         if self.lenth / self.size >= 0.7:
    #             self.resize()
    #     else:
    #         if self.slots[hashvalue] == key:
    #             self.data[hashvalue] = data
    #         else:
    #             while self.slots[hashvalue] != None and self.slots[hashvalue] != key:
    #                 hashvalue = self.rehash(hashvalue)
    #             if self.slots[hashvalue] == None:
    #                 self.slots[hashvalue] = key
    #                 self.data[hashvalue] = data
    #                 self.lenth += 1
    #                 if self.lenth / self.size >= 0.7:
    #                     self.resize()
    #             else:
    #                 self.data[hashvalue] = data
    
    def get(self, key):
        startvalue = self.hashfunction(key)
        position = startvalue

        while self.slots[position] != None:
            if self.slots[position] == key:
                return self.data[position]
            position = self.rehash(position)
            if position == startvalue:
                return None
        return None

    def resize(self):
        old_slots = self.slots
        old_data = self.data

        # 计算新的容量
        old_size = self.size
        target_size = old_size * 2 + 1 # 目标两倍大，加一保证是基数
        self.size = self.nextprime(target_size) # 用 nextprime 计算下一个质数
        print(f'Load: {self.lenth / old_size:.2f}, collision rate: {self.collisions/self.lenth:.2f}. Resizing from {old_size} to {self.size}')

        # 重置哈希表
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.collisions = 0

        # 将旧数据插入到新哈希表中
        for i in range(len(old_slots)):
            if old_slots[i] is not None:
                newhashvalue = self.hashfunction(old_slots[i])
                while self.slots[newhashvalue] is not None:
                    newhashvalue = self.rehash(newhashvalue)
                self.slots[newhashvalue] = old_slots[i]
                self.data[newhashvalue] = old_data[i]

    def nextprime(self, num):
        if num % 2 == 0:
            num += 1
        else:
            num += 2
        sqr = int(num ** 0.5) + 1
        for i in range(2, sqr):
            if num % i == 0:
                return self.nextprime(num)
        return num
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        return self.put(key, data)
    
    def __len__(self):
        return self.lenth


if __name__ == '__main__':
    from random import randint

    h = HashTable(50,0.5)

    lst = []
    for i in range(200000):
        num = randint(1,10000000)
        lst.append(num)
        h.put(num, 'v' + str(i))

    print(f'lst-len:{len(lst)}, unique keys:{len(set(lst))}')
    print(f'load: {h.lenth / h.size * 100:.0f}%')
    print(f'collision: {h.collisions / h.lenth*100:.0f}%')