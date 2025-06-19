from job import Job

MAX_QUEUE_SIZE = 10
AGING_INTERVAL = 5
EXPIRY_TIME = 20
TICKS_TO_SIMULATE = 10

INITIAL_JOBS = [
    Job(user_id=1, job_id=101, priority=2, created_at=0),
    Job(user_id=2, job_id=102, priority=1, created_at=0),
]
