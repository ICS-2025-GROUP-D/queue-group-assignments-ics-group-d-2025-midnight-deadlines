from queue_manager import PrintQueueManager
from config import INITIAL_JOBS, TICKS_TO_SIMULATE

def main():
    manager = PrintQueueManager()

    for job in INITIAL_JOBS:
        manager.enqueue_job(job.user_id, job.job_id, job.priority)

    for _ in range(TICKS_TO_SIMULATE):
        manager.tick()
        manager.show_status()

if __name__ == "__main__":
    main()
