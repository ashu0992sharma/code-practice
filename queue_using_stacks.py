class Queue():
    
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, data):
        self.in_stack.append(data)
    
    def dequeue(self):
        return self.in_stack.pop()
    
    def display(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[0]



q1 = Queue()
q = int(input())
for i in range(q):
    
    a = list(map(int, input().split(" ")))
 
    if a[0] == 1:
        q1.enqueue(a[1])
       
    elif a[0] == 2:
        q1.dequeue()
        
    else:
        print(q1.display())
            
