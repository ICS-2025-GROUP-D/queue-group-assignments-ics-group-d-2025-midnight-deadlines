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
        self.current_job = None

    def enqueue_job(self, user_id, job_id, priority):
        current_time = self.tick_simulator.get_time()
        job = Job(user_id, job_id, priority, created_at=current_time)
        self.queue.enqueue(job)
        print(
            f"Job {job.job_id} enqueued with priority {job.priority} at tick {current_time}"
        )

    def dequeue_job(self):
        if self.queue.is_empty():
            print("Queue is empty")
        else:
            job = self.queue.dequeue()
            print(job)

    def apply_priority_aging(self, current_tick=None):
        if current_tick is None:
            current_tick = self.tick_simulator.get_time()
        self.priority.apply_priority_aging(current_tick)

    def remove_expired_jobs(self):
        current_tick = self.tick_simulator.get_time()
        self.expiry.remove_expired_jobs(current_tick)

    def handle_simultaneous_submissions(self, jobs):
        self.submitter.submit_jobs(jobs)

    def print_job(self):
        self.visualizer.display_queue()

    def process_next_job(self):
        if self.queue.is_empty():
            print("Printer is idle.")
            self.current_job: Job = None
        else:
            self.current_job = self.queue.dequeue()
            print(
                f"Printing job {self.current_job.job_id} from user {self.current_job.user_id} (Priority: {self.current_job.priority})"
            )

    def tick(self):
        self.tick_simulator.tick()
        current_tick = self.tick_simulator.get_time()
        self.tick_simulator.update_wait_times(current_tick)
        # Apply priority aging & reorder
        self.apply_priority_aging(current_tick)
        self.remove_expired_jobs()
        # Process job at front (simulate printing)
        self.process_next_job()
        self.show_status()

    def show_status(self):
        self.visualizer.display_queue()