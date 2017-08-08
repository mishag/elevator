from threading import Condition, Lock, Thread
from collections import deque
from job import Job
import time


class Elevator(Thread):
    def __init__(self, name, speed=1.0, wait_time=1.0):
        super(Elevator, self).__init__()
        self._location = 0
        self._queue = deque()
        self._lock = Lock()
        self._cond_have_work = Condition(self._lock)
        self._num_secs_per_floor = speed
        self._num_secs_at_floor = wait_time
        self._name = name

    @property
    def location(self):
        return self._location

    @property
    def name(self):
        return self._name

    @property
    def current_queue_size(self):
        with self._lock:
            return len(self._queue)

    def add_trip(self, trip):
        with self._lock:
            print("Elevator {} queueing trip {}, queue size: {}"
                  .format(self.name, trip, len(self._queue) + 1))
            for job in self._queue:
                if job.add_trip(trip):
                    self._cond_have_work.notify()
                    return

            self._queue.append(Job(trip))
            self._cond_have_work.notify()

    def _move(self, start, end, step):

        print("Elevator {} going from floor {} to floor {}"
              .format(self.name, start, end))

        end = end + 1 if step > 0 else end - 1
        for stop in range(start, end, step):
            self._location = stop
            time.sleep(self._num_secs_per_floor)

        print("Elevator {} stopped on floor {}"
              .format(self.name, self._location))

        time.sleep(self._num_secs_at_floor)

    def _execute_job(self, job):
        step = job.direction
        for stop in job.stops:
            self._move(self._location, stop, step)

    def run(self):
        print("Elevator {} starting to run".format(self.name))
        while True:
            with self._lock:

                while len(self._queue) == 0:
                    self._cond_have_work.wait()

                job = self._queue.popleft()

            self._execute_job(job)
