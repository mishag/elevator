import time
from threading import Thread


class Elevator(Thread):
    """
    speed:     speed to travel between floors in seconds per floor
    wait_time: time to wait on each floor in seconds
    """

    def __init__(self,
                 name,
                 job_queue,
                 speed=1,
                 wait_time=1,
                 starting_floor=0):
        super(Elevator, self).__init__()

        self._job_queue = job_queue
        self._speed = speed
        self._wait_time = wait_time
        self._current_floor = starting_floor
        self._idle = True
        self._name = name

    @property
    def current_floor(self):
        return self._current_floor

    @property
    def idle(self):
        return self._idle

    @property
    def speed(self):
        return self._speed

    @property
    def wait_time(self):
        return self._wait_time

    @property
    def name(self):
        return self._name

    def _goto_floor(self, target):
        step = 1 if target > self._current_floor else -1

        while self._current_floor != target:
            time.sleep(self._speed)
            self._current_floor += step

        print("Elevator {} at floor {}\n".format(self.name,
                                                 self.current_floor))
        time.sleep(self._wait_time)

    def _execute_job(self, job):
        self._idle = False
        stops = job.stops
        print("Elevator {} executing job {}".format(self.name, job))

        for floor in stops:
            print("Elevator {} going to floor {}\n".format(self.name, floor))
            self._goto_floor(floor)

        self._idle = True

    def run(self):
        while True:
            job = self._job_queue.pop()
            self._execute_job(job)
