import sys
class Q:
    def __init__(self):
        self.firstElement = None
        self.finalElement = None
        self.cnt = 0
    
    def push(self, data):
        e = element(data)
        if self.firstElement == None:
            self.firstElement = e
            self.finalElement = e
            self.cnt += 1
            return
        self.finalElement.nextElement = e
        self.finalElement = e
        self.cnt += 1
        
    def pop(self):
        if self.firstElement == None:
            return -1
        val = self.firstElement.data
        tmp = self.firstElement.nextElement
        self.firstElement = None
        self.firstElement = tmp
        if self.firstElement == None:
            self.finalElement = None
        self.cnt -= 1
        return val
    
    def size(self):
        return self.cnt
    
    def empty(self):
        if self.firstElement == None:
            return 1
        return 0
    
    def front(self):
        if self.firstElement == None:
            return -1
        return self.firstElement.data
    
    def back(self):
        if self.finalElement == None:
            return -1
        return self.finalElement.data
    
class element:
    def __init__(self, Data):
        self.data = Data
        self.prevElement = None
        self.nextElement = None
        pass

a = int(sys.stdin.readline())
queue = Q()
result = []
for i in range(a):
    inputs = sys.stdin.readline().split()
    instruction = inputs[0]
    val = 0
    if len(inputs) > 1:
        val = int(inputs[1])
        
    if instruction == 'push':
        queue.push(data=val)
    if instruction == 'pop':
        result.append(queue.pop())
    if instruction == 'size':
        result.append(queue.size())
    if instruction == 'empty':
        result.append(queue.empty())
    if instruction == 'front':
        result.append(queue.front())
    if instruction == 'back':
        result.append(queue.back())

for i in result:
    print(i)