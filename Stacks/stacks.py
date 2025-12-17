class Stack:
    def __init__(self,capacity = 10):
        self.items = []
        self.capacity = capacity
        self.stk = [0] * capacity
        self.top = -1
    def push(self, data):
        if self.isFull():
            print("Stack overflow")
        else:
            self.top += 1
            self.stk[self.top] = data

    def pop(self):
        if self.isEmpty():          
            print("Stack underflow")
            return -1
        temp = self.stk[self.top]
        self.top -= 1
        return temp

    def isFull(self):
        return self.top == self.capacity - 1

    def isEmpty(self):
        return self.top == -1

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return -1
        return self.stk[self.top]

Stk = Stack(5)
Stk.push(10)
Stk.push(20)
Stk.push(30)
Stk.push(40)
Stk.push(50) 
print(Stk.peek())
print(Stk.pop())
print(Stk.peek())


'''
# Problem - we are evaluating expression like bracket like scientific calculation and all that 
# exp = " {()}" - valid 
# exp = " {()"} "  # invalid
# how can we solve this problem using stack 
#Using recursion, we repeatedly remove valid bracket pairs ((), {}, []) and then call the function again on the smaller string.
# If the string becomes empty, it’s valid; if no pairs can be removed but characters remain, it’s invalid. '''

