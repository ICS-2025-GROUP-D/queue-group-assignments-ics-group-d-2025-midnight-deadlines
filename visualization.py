class Visualizer:
    @staticmethod
    def display_queue(jobs):
        """Display a formatted snapshot of the queue state."""
        if not jobs:
            print("Queue is empty.")
            return

        # Sort jobs by priority (descending) and waiting time (descending)
        sorted_jobs = sorted(jobs, key=lambda x: (-x['priority'], -x['waiting_time']))

        print("\n=== Print Queue Snapshot ===")
        print(f"{'Job ID':<10} {'User ID':<10} {'Priority':<10} {'Waiting Time':<12}")
        print("-" * 42)
        for job in sorted_jobs:
            print(f"{job['job_id']:<10} {job['user_id']:<10} {job['priority']:<10} {job['waiting_time']:<12}")
        print("==========================\n")

# Example usage (for testing)
if __name__ == "__main__":
    test_jobs = [
        {'user_id': 'user1', 'job_id': 'job1', 'priority': 2, 'waiting_time': 5},
        {'user_id': 'user2', 'job_id': 'job2', 'priority': 1, 'waiting_time': 3},
        {'user_id': 'user3', 'job_id': 'job3', 'priority': 2, 'waiting_time': 1}
    ]
    Visualizer.display_queue(test_jobs)