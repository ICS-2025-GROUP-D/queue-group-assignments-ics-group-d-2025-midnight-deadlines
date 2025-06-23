class PriorityManager:
    def __init__(self, queue, aging_threshold=5):
        self.queue = queue
        self.aging_threshold = aging_threshold

    def apply_priority_aging(self, current_tick: int):
        for job in self.queue.items:
            job["waiting_time"] = current_tick - job["arrival_tick"]

            if job["waiting_time"] > self.aging_threshold:
                job["priority"] += 1

        self.reorder_queue()

    def reorder_queue(self):
        self.queue.items.sort(
            key=lambda job: (-job["priority"], -job["waiting_time"])
        )
