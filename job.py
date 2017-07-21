UP = 1
DOWN = -1


class Trip(object):
    def __init__(self, start, end):
        if start == end:
            raise ValueError("start must not equal end")

        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def direction(self):
        return UP if self._start - self._end < 0 else DOWN

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __hash__(self):
        return hash((self.start, self.end))

    def __repr__(self):
        return "[ {} => {} ]".format(self.start, self.end)

    def __str__(self):
        return "[ {} => {} ]".format(self.start, self.end)

    def is_subordinate_to(self, other):
        if self.direction != other.direction:
            return False

        if self.direction == UP:
            return other.start >= self.start and other.end <= self.end

        return other.start <= self.start and other.end >= self.end


class Job(object):
    def __init__(self, root_trip):
        self._root = root_trip
        self._trips = set([root_trip])
        self._stops = set([root_trip.start, root_trip.end])

    @property
    def direction(self):
        return self._root.direction

    def add_trip(self, trip):
        if not trip.is_subordinate_to(self._root):
            return False

        self._trips.add(trip)
        self._stops.add(trip.start)
        self._stops.add(trip.end)

        return True

    def __repr__(self):
        return "[ Stops: {} ]".format(self.stops)

    def __str__(self):
        return "[ Stops: {} ]".format(self.stops)

    @property
    def stops(self):
        return sorted(self._stops, reverse=(self.direction == DOWN))
