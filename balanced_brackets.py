#!/bin/python3

import sys
class Stack():
    
    def __init__(self):
        self.table = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        self.stack = []
    
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        return self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def  display(self):
        for data in self.stack:
            print(data)
            

t = int(input().strip())

for a0 in range(t):
    stack = Stack()
    s = input().strip()
    for data in s:
        if data not in stack.table or stack.isEmpty():
            stack.push(data)
        else:
  
            if stack.table[data] == stack.stack[-1]:
                stack.pop()
            else:
                break
                stack.push(data)
        
    

    if not stack.isEmpty():

        print('NO')
    else:
        print('YES')

