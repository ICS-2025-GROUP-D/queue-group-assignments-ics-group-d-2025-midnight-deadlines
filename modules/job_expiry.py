from config import EXPIRY_TIME

class JobExpiryManager:
    def __init__(self, queue):
        self.queue=queue

    def remove_expired_jobs(self, current_tick):
        non_expired_jobs = []

        while not self.queue.is_empty():
            job = self.queue.dequeue()
            print(f"Checking job {job.job_id} with wait time {job.wait_time}")

            job.wait_time= current_tick- job.created_at
            if job.wait_time >= EXPIRY_TIME:
                print(f"Job{job.job_id} from user {job.user_id}expired after {job.wait_time} ticks and was removed.")

            else:
                non_expired_jobs.append(job)

        for job in non_expired_jobs:
                self.queue.enqueue(job)