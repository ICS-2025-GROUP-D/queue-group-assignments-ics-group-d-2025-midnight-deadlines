
from modules.queue import CircularQueue
from modules.priority_aging import PriorityManager
from modules.job_expiry import JobExpiryManager
from modules.concurrent_submission import SubmissionManager
from modules.event_simulator import TickSimulator
from modules.visualization import Visualizer

class PrintQueueManager:
    def __init__(self):
        self.queue = CircularQueue()
        self.priority = PriorityManager(self.queue)
        self.expiry = JobExpiryManager(self.queue)
        self.submitter = SubmissionManager(self.queue)
        self.tick_simulator = TickSimulator(self.queue)
        self.visualizer = Visualizer(self.queue)

    def enqueue_job(self, user_id, job_id, priority):...
    def apply_priority_aging(self):...
    def remove_expired_jobs(self):...
    def handle_simultaneous_submissions(self, jobs):...
    def print_job(self):...
    def tick(self):...
    def show_status(self):...

class PrintQueueManager:
    def __init__(self):
        self.queue = []
        self.time = 0
        self.aging_interval = 3
        self.expiry_limit = 10
        self.last_aging_tick = 0

    def tick(self):
        self.time += 1
        print(f"Tick {self.time}")
        for job in self.queue:
            job["waiting_time"] += 1
        if (self.time - self.last_aging_tick) >= self.aging_interval:
            print("Applying priority aging...")
            self.apply_priority_aging()
            self.last_aging_tick = self.time
        print("Checking for expired jobs...")
        self.remove_expired_jobs()
        self.show_status()

    def apply_priority_aging(self):
        for job in self.queue:
            job["priority"] += 1
            print(f"Job {job['job_id']} priority increased to {job['priority']}")

    def remove_expired_jobs(self):
        expired = [job for job in self.queue if job["waiting_time"] >= self.expiry_limit]
        for job in expired:
            print(f"Job {job['job_id']} expired and removed after waiting {job['waiting_time']} ticks.")
            self.queue.remove(job)

    def show_status(self):
        print("Queue Status:")
        if not self.queue:
            print("  (Queue is empty)")
        else:
            for job in self.queue:
                print(f"  Job {job['job_id']} | Priority: {job[']()_]()

