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
    def show_status(self):
        """Display a formatted snapshot of the queue state, sorted by priority and waiting time."""
        if self.size == 0:
            print("Queue is empty.")
            return

        # Collect valid jobs
        jobs = []
        index = self.front
        for _ in range(self.size):
            if self.queue[index] is not None:
                jobs.append(self.queue[index])
            index = (index + 1) % self.capacity

        # Sort jobs by priority (descending) and waiting time (descending) for tie-breaking
        sorted_jobs = sorted(jobs, key=lambda x: (-x['priority'], -x['waiting_time']))

        # Print formatted table
        print("\n=== Print Queue Snapshot ===")
        print(f"{'Job ID':<10} {'User ID':<10} {'Priority':<10} {'Waiting Time':<12}")
        print("-" * 42)
        for job in sorted_jobs:
            print(f"{job['job_id']:<10} {job['user_id']:<10} {job['priority']:<10} {job['waiting_time']:<12}")
        print("==========================\n")