from job import Job
from modules.queue import CircularQueue
from modules.priority_aging import PriorityManager
from modules.job_expiry import JobExpiryManager
from modules.concurrent_submission import SubmissionManager
from modules.event_simulator import TickSimulator
from modules.visualization import Visualizer

class PrintQueueManager:
    def __init__(self):
        self.queue = CircularQueue()
        self.time=0
        self.priority = PriorityManager(self.queue)
        self.expiry = JobExpiryManager(self.queue)
        self.submitter = SubmissionManager(self)
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

    def remove_expired_jobs(self):
        self.expiry.remove_expired_jobs(current_tick=self.time)



    def handle_simultaneous_submissions(self, jobs):...
    def print_job(self):...
    def tick(self):...
    def show_status(self):...