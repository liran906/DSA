import sys
sys.path.append('.')
from pythonds.basic.deque import Deque

def palCheck(string):
    dq = Deque()

    for i in str(string):
        dq.addRear(i)
    
    while dq.size() > 1:
        if dq.removeFront() != dq.removeRear():
            return False
    return True

if __name__ == '__main__':
    print(palCheck('radar'))
    print(palCheck('上海自来水来自海上'))
    print(palCheck('10010001'))