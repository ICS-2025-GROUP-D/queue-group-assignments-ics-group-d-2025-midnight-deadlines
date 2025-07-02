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
        self.tick_simulator = TickSimulator(self.queue)
        self.priority = PriorityManager(self.queue)
        self.expiry = JobExpiryManager(self.queue)
        self.submitter = SubmissionManager(self)
        self.visualizer = Visualizer(self.queue)
        self.current_job=None

    def enqueue_job(self, user_id, job_id, priority):
        current_time=self.tick_simulator.get_time()
        job= Job(user_id,job_id,priority,created_at=current_time)
        self.queue.enqueue(job)
        print(f"job{job.job_id} enqueued with priority {job.priority} at tick {current_time}")

    def dequeue_job(self):
        if self.queue.is_empty():
            print("Queue is empty")
        else:
            job=self.queue.dequeue()
            print(job)

    def apply_priority_aging(self):...

    def remove_expired_jobs(self):
        self.expiry.remove_expired_jobs(current_tick=self.time)

    def handle_simultaneous_submissions(self, jobs):
        self.submitter.submit_jobs(jobs)

    def print_job(self):
        self.visualizer.display_queue()

    def tick(self):
        self.time += 1
        print(f" Tick {self.time}")

        temp_queue = CircularQueue()
        while not self.queue.is_empty():
            job = self.queue.dequeue()
            job.wait_time = self.time - job.created_at
            temp_queue.enqueue(job)

        while not temp_queue.is_empty():
            self.queue.enqueue(temp_queue.dequeue())

        self.remove_expired_jobs()

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
