from job import Job

#class CircularQueue:
class CircularQueue:
    Default_Capacity = 10

    def __init__(self):
        self._data = [None] * CircularQueue.Default_Capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError("Queue empty")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def get_all_jobs(self):
        jobs=[]
        for i in range (self.size):
            idx= (self._front + i) % len(self._data)
            if self._data[idx] is not None:
                jobs.append(self._data[idx])
        return jobs
    
    def clear(self):
        self.__init__()



   
