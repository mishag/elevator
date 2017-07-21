from queue import JobQueue
from elevator import Elevator
from job import Trip

import random
import time


class Simulator(object):
    def __init__(self,
                 num_elevators=4,
                 num_floors=10):

        self._num_elevators = num_elevators
        self._num_floors = num_floors
        self._job_queue = JobQueue()

        random.seed()

    @property
    def num_elevators(self):
        return self._num_elevators

    @property
    def num_floors(self):
        return self._num_floors

    def _start_elevators(self):
        for i in range(self._num_elevators):
                elevator = Elevator(str(i), self._job_queue)
                elevator.start()

    def _generate_trip(self):
        start = 0
        end = 0
        while start == end:
            start = random.randint(0, self.num_floors - 1)
            end = random.randint(0, self.num_floors - 1)

        return Trip(start, end)

    def run(self):
        self._start_elevators()
        while True:
            pause = random.randint(1, 2)
            print("Waiting for next trip for {} seconds...\n".format(pause))
            time.sleep(pause)
            trip = self._generate_trip()
            print("Got trip {}, queue size is {}\n".format(
                trip, len(self._job_queue)))
            self._job_queue.submit(trip)
