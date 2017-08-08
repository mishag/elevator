from collections import deque
from threading import Lock, Condition

from job import Job


class JobQueue(object):
    def __init__(self):
        self._queue = deque()
        self._lock = Lock()
        self._cond_not_empty = Condition(self._lock)

    def __len__(self):
        with self._lock:
            return len(self._queue)

    def submit(self, trip):
        trip_added = False
        with self._lock:
            for job in reversed(self._queue):
                if job.add_trip(trip):
                    trip_added = True
                    break

            if not trip_added:
                self._queue.append(Job(trip))

            self._cond_not_empty.notify()

    def pop(self):
        with self._lock:
            while len(self._queue) == 0:
                self._cond_not_empty.wait()

            assert len(self._queue) > 0

            return self._queue.popleft()
