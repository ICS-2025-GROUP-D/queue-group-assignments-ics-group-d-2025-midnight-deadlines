class Job:
    def __init__(self, user_id: int, job_id: int, priority: int, created_at: int):
        self.user_id = user_id
        self.job_id = job_id
        self.priority = priority
        self.created_at = created_at
        self.wait_time = 0