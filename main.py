from queue_manager import PrintQueueManager
from config import INITIAL_JOBS, TICKS_TO_SIMULATE
from job import Job


def submit_initial_jobs(manager: PrintQueueManager):
    print("Submitting initial jobs...")
    manager.handle_simultaneous_submissions(INITIAL_JOBS)


def submit_additional_jobs(manager: PrintQueueManager, current_tick):
    """
    Dynamically submit new jobs at specific ticks.
    Example: Simulate new jobs arriving at tick 5.
    """
    if current_tick == 5:
        print("\nNew jobs submitted at tick 5:")
        new_jobs = [
            Job(user_id=3, job_id=103, priority=2, created_at=current_tick),
            Job(user_id=4, job_id=104, priority=1, created_at=current_tick),
        ]
        manager.handle_simultaneous_submissions(new_jobs)


def simulate(manager: PrintQueueManager, ticks: int):
    for tick in range(ticks):
        submit_additional_jobs(manager, tick)
        manager.tick()


def main():
    manager = PrintQueueManager()
    submit_initial_jobs(manager)
    simulate(manager, TICKS_TO_SIMULATE)


if __name__ == "__main__":
    main()
