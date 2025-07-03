class TickSimulator:
    def __init__(self, queue):
        self.queue = queue
        self.current_time = 0

    def tick(self): 
        self.current_time += 1
        print(f"\n Tick {self.current_time}")
    def get_time(self):
        return self.current_time    
    
    def update_wait_times(self, current_tick=None):
        if current_tick is None:
            current_tick = self.current_time
        for job in self.queue.items:
            job.wait_time = current_tick - job.created_at
                
