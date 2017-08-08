from elevator import Elevator
from dispatcher import Dispatcher
from job import Trip

import random
import time


class Simulator(object):

    def __init__(self,
                 num_floors=10,
                 num_elevators=2,
                 elevator_speed=1.0,
                 elevator_wait_time=1.0):

        self._elevator_speed = elevator_speed
        self._elevator_wait_time = elevator_wait_time
        self._elevators = []
        self._dispatcher = Dispatcher(self._elevators)
        self._num_floors = num_floors

        for i in range(num_elevators):
            self._elevators.append(Elevator(str(i),
                                            self._elevator_speed,
                                            self._elevator_wait_time))

    def _generate_trip(self):
        start = 0
        end = 0
        while start == end:
            start = random.randint(0, self._num_floors - 1)
            end = random.randint(0, self._num_floors - 1)

        return Trip(start, end)

    def run(self):
        for e in self._elevators:
            e.start()

        while True:
            pause = random.randint(1, 2)
            time.sleep(pause)
            trip = self._generate_trip()
            print("Got trip {}".format(trip))
            self._dispatcher.submit(trip)


if __name__ == "__main__":
    simulator = Simulator()
    simulator.run()
