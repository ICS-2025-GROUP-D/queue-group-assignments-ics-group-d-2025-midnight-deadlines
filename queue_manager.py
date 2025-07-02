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

    def enqueue_job(self, user_id, job_id, priority):...
    def apply_priority_aging(self, current_tick=None):
        if current_tick is None:
            current_tick = self.tick_simulator.get_time()
        self.priority.apply_priority_aging(current_tick)
    def remove_expired_jobs(self):...
    def handle_simultaneous_submissions(self, jobs):...
    def print_job(self):...
    def tick(self):
        self.tick_simulator.increment_time()
        current_tick = self.tick_simulator.get_time()

        self.apply_priority_aging(current_tick)
        self.remove_expired_jobs()
        self.show_status()
    def show_status(self):...
