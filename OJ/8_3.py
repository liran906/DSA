class HashTable:
    def __init__(self, size=11):
        self.size = self.resize(size - 1)
        self.keys = [None] * self.size
        self.values = [None] * self.size     
    
    def hashfunc(self, key):
        return key % self.size
    
    def rehash(self, oldhash):
        return (oldhash + 1) % self.size
    
    def put(self, key, value):
        pos = self.hashfunc(key)
        startpos = pos

        while self.keys[pos] != None and self.keys[pos] != key:
            pos = self.rehash(pos)
            if pos == startpos: # 遍历一圈
                raise Exception("HashTable is full")

        if self.keys[pos] == None:
            self.keys[pos] = key
            self.values[pos] = value
        else:
            self.values[pos] = value
    
    def get(self, key):
        pos = self.hashfunc(key)
        startpos = pos

        while self.keys[pos] != None and self.keys[pos] != key:
            pos = self.rehash(pos)
            if pos == startpos:
                return None
        if self.keys[pos] == None:
            return None
        else:
            return self.values[pos]
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        return self.put(key, value)

def isPrime(num):
    # 求最小质数
    pass

def createHashTable(n):
    return HashTable(n)

def insertNumbers(table, nums):
    # code here
    pass

n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
insertNumbers(table, nums)