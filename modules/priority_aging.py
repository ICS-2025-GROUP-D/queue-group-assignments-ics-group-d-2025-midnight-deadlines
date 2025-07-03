class PriorityManager:
    def __init__(self, queue, aging_threshold=5):
        self.queue = queue
        self.aging_threshold = aging_threshold

    def apply_priority_aging(self, current_tick: int):
        jobs = self.queue.get_all_jobs()

        for job in jobs:
            job.wait_time = current_tick - job.created_at

            if job.wait_time > self.aging_threshold:
                job.priority += 1

        self.reorder_queue(jobs)

    def reorder_queue(self, jobs):
        # Sort jobs by priority (descending), then wait_time (descending)
        jobs.sort(key=lambda job: (-job.priority, -job.wait_time))

        # Clear and rebuild the queue
        self.queue.clear()
        for job in jobs:
            self.queue.enqueue(job)