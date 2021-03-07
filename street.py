class Street(object):
    def __init__(self, start_intersection = -1, end_intersection = -1, name = "default_name", duration = -1):
        self.name = name
        self.start_intersection = start_intersection
        self.end_intersection = end_intersection
        self.duration = duration
        self.t = -1


class Car(object):
    def __init__(self, streets: list):
        self.streets = streets
        self.progress = 0
        self.curr_street = streets[0]

    def drive(self):
        self.progress += 1
        self.curr_street = self.streets[self.progress]

        