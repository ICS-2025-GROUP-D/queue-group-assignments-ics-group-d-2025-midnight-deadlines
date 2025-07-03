# Group : `midnight-deadlines`

## 👥 Members & Modules

Each member was responsible for a module and contributed their function into the shared `PrintQueueManager` class:

| Name              | No.           | Module                             | Contribution                                                                                   |
| ----------------- | ---------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Richie Mwangi** | 189293 | Core Queue Management              | Built the circular queue (`queue.py`) with enqueue, dequeue, and job metadata handling.        |
| **Ernest Njoroge**  | 190023 | Priority & Aging System            | Implemented job priority sorting, aging, and wait-time tie-breaking (`priority_aging.py`).     |
| **Lynn Ivy** | 175793 | Job Expiry & Cleanup               | Developed logic to expire and remove old jobs after threshold (`job_expiry.py`).               |
| **Joseph Kinyuru**   | 167600 | Concurrent Submission Handling     | Ensured thread-safe, simultaneous job addition with proper locks (`concurrent_submission.py`). |
| **Jean Njoroge**  | 187923 | Event Simulation & Time Management | Handled tick events, wait-time updates, and triggered aging/expiry (`event_simulator.py`).     |
| **Laureen Angie**  | 191876 | Visualization & Reporting          | Created clear visual snapshots of queue state after every event (`visualization.py`).          |

---

## 📁 Project Structure

```
main.py
config.py
job.py
queue_manager.py
modules/
├── queue.py
├── priority_aging.py
├── job_expiry.py
├── concurrent_submission.py
├── event_simulator.py
├── visualization.py
```

---

## ▶️ How to Run

Make sure Python 3.10+ is installed.

```bash
python3 main.py
```

This will start the Print Queue Simulator and process events as defined in the main script.
