# https://docs.python.org/3/library/threading.html
import threading
from job import Job

class SubmissionManager:
    def __init__(self, queue_manager):
        self.queue_manager = queue_manager
        self.lock = threading.Lock()

    def submit_jobs(self, jobs: list[Job]):
        """
        Launches multiple threads to enqueue jobs concurrently.
        Ensures thread-safe access to the queue using a lock -- prevents race condition.
        """
        threads = []

        for job in jobs:
            thread = threading.Thread(target=self.__submit_single_job, args=(job,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def __submit_single_job(self, job: Job):
        """
        DO NOT CALL OUTSIDE PARENT.
        This method is run by each thread to safely enqueue a job.
        """
        with self.lock:
            self.queue_manager.enqueue_job(job.user_id, job.job_id, job.priority)
