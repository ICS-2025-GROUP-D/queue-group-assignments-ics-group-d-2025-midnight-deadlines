from queue_manager import PrintQueueManager

pq = PrintQueueManager()

pq.queue.append({"job_id": "J1", "priority": 1, "waiting_time": 0})
pq.queue.append({"job_id": "J2", "priority": 2, "waiting_time": 0})

for _ in range(12):
    pq.tick()
