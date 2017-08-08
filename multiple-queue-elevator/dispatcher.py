import math


class Dispatcher(object):
    def __init__(self, elevator_list):
        self._elevators = elevator_list

    def find_least_busy_elevator(self):
        cur_min = math.inf
        min_index = -1
        for i, el in enumerate(self._elevators):
            current_size = el.current_queue_size
            if current_size < cur_min:
                cur_min = current_size
                min_index = i

        return min_index

    def submit(self, trip):
        idx = self.find_least_busy_elevator()
        print("Dispatching trip {} to elevator {}"
              .format(trip, self._elevators[idx].name))
        self._elevators[idx].add_trip(trip)
