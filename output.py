class Simulation(object):
    def __init__(self):
        self.intersections = []


class SimulatedIntersection(object):
    def __init__(self):
        self.intersection = None
        self.streets = []

class SimulatedStreet(object):
    def __init__(self):
        self.street = None
        self.timeGreenLight = -1

class TrafficLightSchedule(object):
    def __init__(self, intersection, streets, duration):
        self.intersection = intersection
        self.streets = streets
        self.duration = duration