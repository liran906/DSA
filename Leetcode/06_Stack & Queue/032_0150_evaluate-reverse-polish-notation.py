class Solution(object):
    def evalRPN(self, tokens):
        s = []
        for t in tokens:
            if t not in '+-*/':
                s.append(int(t))
            else:
                op2 = s.pop()
                op1 = s.pop()
                s.append(self.doMath(op1,op2,t))
        return s.pop()
                
    def doMath(self, op1, op2, o):
        if o == '+':
            return op1 + op2
        elif o == '-':
            return op1 - op2
        elif o == '*':
            return op1 * op2
        else:
            return int(op1 / op2)

s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))