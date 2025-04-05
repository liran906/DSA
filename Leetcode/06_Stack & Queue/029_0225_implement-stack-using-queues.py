class MyStack(object):
    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        for i in range(len(self.q)):
            cur = self.q.pop(0)
            if i == len(self.q): # 这里是等于len因为pop之后len已经-1了
                return cur
            self.q.append(cur)

    def top(self):
        for i in range(len(self.q)):
            cur = self.q.pop(0)
            self.q.append(cur)
        return cur
            

    def empty(self):
        return not self.q