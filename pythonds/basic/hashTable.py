class HashTable:
    def __init__(self, size=11, load_factor=0.65):
        """
        初始化哈希表
        :param size: 初始哈希表大小（会被调整为下一个质数）
        :param load_factor: 负载因子，超过此值时扩容
        """
        self.size = self.nextprime(size - 1)  # 计算最接近的质数作为哈希表大小
        self.slots = [None] * self.size  # 存储键
        self.data = [None] * self.size  # 存储值
        self.load_factor = load_factor  # 负载因子
        self.lenth = 0  # 当前存储的键值对数量
        self.collisions = 0  # 记录冲突次数

    def hashfunction(self, key):
        """
        计算哈希值（取模法）
        :param key: 需要存储的键
        :return: 哈希索引
        """
        return key % self.size

    def rehash(self, oldhash):
        """
        线性探测法处理哈希冲突
        :param oldhash: 旧哈希值
        :return: 新哈希索引
        """
        return (oldhash + 1) % self.size

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

    def put(self, key, data):
        """
        插入键值对
        :param key: 键
        :param data: 值
        """
        hashvalue = self.hashfunction(key)  # 计算哈希值

        # 处理哈希冲突（线性探测）
        if self.slots[hashvalue] is not None:
            self.collisions += 1  # 记录冲突次数
            while self.slots[hashvalue] is not None:
                if self.slots[hashvalue] == key:  # 如果找到相同的 key，则更新值
                    self.data[hashvalue] = data
                    return
                hashvalue = self.rehash(hashvalue)  # 线性探测找下一个空位

        # 找到空槽，插入新键值对
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
        self.lenth += 1

        # 超过负载因子，执行扩容
        if self.lenth / self.size >= self.load_factor:
            self.resize()

    def get(self, key):
        """
        通过 key 获取对应的值
        :param key: 查询的键
        :return: 对应的值，若不存在则返回 None
        """
        startvalue = self.hashfunction(key)  # 计算哈希值
        position = startvalue

        # 线性探测查找 key
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            position = self.rehash(position)  # 继续探测下一个位置
            if position == startvalue:  # 遍历一圈回到起点，说明 key 不存在
                return None
        return None

    def resize(self):
        """
        动态扩展哈希表（容量加倍后取下一个质数）
        """
        old_slots = self.slots  # 备份旧键
        old_data = self.data  # 备份旧值

        # 计算新的哈希表大小
        old_size = self.size
        target_size = old_size * 2 + 1  # 目标大小为原来的两倍加一
        self.size = self.nextprime(target_size)  # 找到最近的质数作为新大小
        print(f'Load: {self.lenth / old_size:.2f}, collision rate: {self.collisions/self.lenth:.2f}. Resizing from {old_size} to {self.size}')

        # 重置哈希表
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.collisions = 0  # 重置冲突计数

        # 重新插入旧数据
        for i in range(len(old_slots)):
            if old_slots[i] is not None:
                newhashvalue = self.hashfunction(old_slots[i])
                if self.slots[newhashvalue] is not None:
                    self.collisions += 1 # 重新计算冲突数
                    while self.slots[newhashvalue] is not None:
                        newhashvalue = self.rehash(newhashvalue)
                self.slots[newhashvalue] = old_slots[i]
                self.data[newhashvalue] = old_data[i]

    def nextprime(self, num):
        """
        计算大于 num 的下一个质数
        :param num: 起始数字
        :return: 最近的质数
        """
        if num % 2 == 0:
            num += 1
        else:
            num += 2
        sqr = int(num ** 0.5) + 1
        for i in range(2, sqr):
            if num % i == 0:
                return self.nextprime(num)  # 递归寻找下一个质数
        return num

    def __getitem__(self, key):
        """
        允许通过 h[key] 方式获取值
        """
        return self.get(key)

    def __setitem__(self, key, data):
        """
        允许通过 h[key] = data 方式插入值
        """
        return self.put(key, data)

    def __len__(self):
        """
        返回哈希表当前存储的键值对数量
        """
        return self.lenth


if __name__ == '__main__':
    from random import randint
    from time import time

    h = HashTable(50, 0.7)  # 初始化哈希表，初始大小 50，负载因子 0.5

    start = time()
    # lst = []
    for i in range(200000):
        num = randint(1, 100000000)  # 生成随机键
        # lst.append(num)
        h.put(num, 'v' + str(i))  # 插入数据
    end = time()

    # print(f'lst-len:{len(lst)}, unique keys:{len(set(lst))}')  # 统计去重后的键数量
    print(f'load: {h.lenth / h.size * 100:.0f}%')  # 打印负载因子
    print(f'collision: {h.collisions / h.lenth * 100:.0f}%')  # 打印冲突率
    print(f'total time spent {end - start:.4f} seconds') # 打印花费时间