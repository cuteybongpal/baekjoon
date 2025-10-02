class priority_queue:
    
    def __init__(self):
        self.heap = []
        pass
    
    def push(self, data):
        self.heap.append(data)
        
        if len(self.heap) == 1:
            return
        idx = len(self.heap) - 1
        while True:
            next_idx = 0
            if idx % 2 == 0:
                next_idx = idx // 2 - 1
            else:
                next_idx = idx // 2
            if next_idx < 0:
                break
            if self.heap[next_idx] < self.heap[idx]:
                self.heap[next_idx], self.heap[idx] = self.heap[idx], self.heap[next_idx]  
                idx = next_idx
            else:
                break
    def pop(self):
        if len(self.heap) == 0:
            return 0
        tmp = self.heap[0]
        if len(self.heap) == 1:
            self.heap.clear()
            return tmp
        self.heap[0] = self.heap.pop()
        cur_idx = 0
        while True:
            next_idx1 = cur_idx * 2 + 1
            next_idx2 = cur_idx * 2 + 2
            if next_idx1 >= len(self.heap):
                break
            elif next_idx2 >= len(self.heap):
                if self.heap[next_idx1] > self.heap[cur_idx]:
                    self.heap[next_idx1], self.heap[cur_idx] = self.heap[cur_idx], self.heap[next_idx1]
                    cur_idx = next_idx1
                    continue
                break
            else:
                if self.heap[next_idx1] <= self.heap[cur_idx] and self.heap[next_idx2] <= self.heap[cur_idx]:
                    break
                
                elif self.heap[next_idx1] >= self.heap[cur_idx]:
                    if self.heap[next_idx1] > self.heap[next_idx2]:
                        self.heap[next_idx1], self.heap[cur_idx] = self.heap[cur_idx], self.heap[next_idx1]
                        cur_idx = next_idx1
                    else:
                        self.heap[next_idx2], self.heap[cur_idx] = self.heap[cur_idx], self.heap[next_idx2]
                        cur_idx = next_idx2
                
                else:
                    if self.heap[next_idx2] > self.heap[next_idx1]:
                        self.heap[next_idx2], self.heap[cur_idx] = self.heap[cur_idx], self.heap[next_idx2]
                        cur_idx = next_idx2
                    else:
                        self.heap[next_idx1], self.heap[cur_idx] = self.heap[cur_idx], self.heap[next_idx1]
                        cur_idx = next_idx1
        return tmp


q = priority_queue()

a = int(input())
result = []
for i in range(a):
    b = int(input())
    if b == 0:
        result.append(q.pop())
    else:
        q.push(b)
for i in result:
    print(i)