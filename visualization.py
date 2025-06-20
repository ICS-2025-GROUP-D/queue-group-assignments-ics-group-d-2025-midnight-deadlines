class Visualizer:
    def __init__(self, queue):
        self.queue = queue

    def display_queue(self):
        if not self.queue:
            print("\nQueue is empty.\n")
            return

        print("\nCurrent Print Queue:")
        print("{:<10} {:<10} {:<10} {:<10}".format("UserID", "JobID", "Priority", "Time"))
        print("-" * 45)

        for job in self.queue:
            print("{:<10} {:<10} {:<10} {:<10}".format(
                job['user_id'], job['job_id'], job['priority'], job['timestamp']
            ))
        print()
