from job import Job
from modules.priority_aging import PriorityManager
from modules.job_expiry import JobExpiryManager
from modules.concurrent_submission import SubmissionManager
from modules.event_simulator import TickSimulator
from modules.visualization import Visualizer

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



class PrintQueueManager:
    def __init__(self):
        self.queue = CircularQueue()
        self.time=0
        self.priority = PriorityManager(self.queue)
        self.expiry = JobExpiryManager(self.queue)
        self.submitter = SubmissionManager(self.queue)
        self.tick_simulator = TickSimulator(self.queue)
        self.visualizer = Visualizer(self.queue)


    def enqueue_job(self, user_id, job_id, priority):
        job= Job(user_id,job_id,priority,self.time)
        self.queue.enqueue(job)

    def dequeue_job(self):
        if self.queue.is_empty():
            print("Queue is empty")
        else:
            job=self.queue.dequeue()
            print(job)


    def apply_priority_aging(self):...
    def remove_expired_jobs(self):...
    def handle_simultaneous_submissions(self, jobs):...
    def print_job(self):...
    def tick(self):...


    def show_status(self):
        temp= CircularQueue()
        if self.queue.is_empty():
            print("Queue is currently empty")

        else:
            while not self.queue.is_empty():
                job = self.queue.dequeue()
                print(job)
                temp.enqueue(job)

        # restores the original queue from temp
        while not temp.is_empty():
            self.queue.enqueue(temp.dequeue())