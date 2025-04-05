class MyQueue(object):
    def __init__(self):
        self.inS = []
        self.outS = []
        
    def push(self, x):
        self.inS.append(x)
    
    def in2out(self):
        while self.inS:
            self.outS.append(self.inS.pop())
        
    def pop(self):
        if self.empty():
            return None
        if not self.outS:
            self.in2out()
        return self.outS.pop()

    def peek(self):
        if self.empty():
            return None
        if not self.outS:
            self.in2out()
        return self.outS[-1]

    def empty(self):
        return (not self.inS) and (not self.outS)