class Visualizer:
    def __init__(self, queue):
        self.queue = queue

    def display_queue(self):
        if self.queue.is_empty():
            print("\nQueue is empty.\n")
            return

        print("\nCurrent Print Queue:")
        print("{:<10} {:<10} {:<10} {:<10}".format("UserID", "JobID", "Priority", "Time"))
        print("-" * 45)

        jobs = self.queue.get_all_jobs()

        for job in jobs:
            print("{:<10} {:<10} {:<10} {:<10}".format(
                job.user_id, job.job_id, job.priority, job.created_at
            ))
        print()