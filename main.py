# sneaky fix going by (⌐■_■)
import sys,os
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
sys.path.append(dir_path)

# We are going to pretend that the code starts here:
import json
import math
from fileManager import FileManager
from street import Car, Street
from output import *

files = ["a", "b", "c", "d", "e", "f"]

def main():
    for filex in files:
        fm = FileManager(dir_path)
        redirect_str = fm.read_file(f"/Input/{filex}.txt")
        #redirect_str = fm.read_file("/Input/demo_input.txt")
        
        input_lines = redirect_str.split("\n")
        line_0 = input_lines[0].split(" ")
        simulation_time = int(line_0[0])
        
        num_intersections = int(line_0[1])
        num_streets = int(line_0[2])
        num_cars = int(line_0[3])
        bonus_points = int(line_0[4])
            
        #print(num_intersections)
        #print(num_intersections)

        streets_dict = {}
        for street_line in input_lines[1:num_streets+1]:
            street_attrs = street_line.split(" ")
            street = Street(int(street_attrs[0]), int(street_attrs[1]), street_attrs[2], int(street_attrs[3]))
            streets_dict[str(street_attrs[2])] = street

        # dict = {intersections: [incoming_streets]}
        intersections = dict()
        for street_name, street in streets_dict.items():
            key = str(street.end_intersection)
            if key not in intersections:
                intersections[key] = [street]
            else:
                incoming_streets = intersections[key]
                if street not in incoming_streets:
                    intersections[key] = incoming_streets + [street]
        print(intersections)

        cars = []
        for car_line in input_lines[num_streets+1:num_streets+1 + num_cars]:
            street_names = car_line.split(" ")[1:]
            streets_objs = [streets_dict[street_name] for street_name in street_names] 
            car = Car(streets_objs)
            cars += [car]
        

        #simulationResult = Simulation()

        schedules = []
        specialCar = cars[0]
        timeProgressed = 0

        for intersection_id, incoming_streets in intersections.items():
            ordered_streets = []
            higher_street = {}
            total_time = 0
            for street in incoming_streets:
                cars_waiting = []
                for car in cars:
                    if car.curr_street == street:
                        cars_waiting.append(car)
                        if(car.progress < len(car.streets) -1):
                            car.drive()
                        else:
                            cars.remove(car)
                street.t = street.duration * len(cars_waiting)
                total_time += street.t
                
                ordered_streets.append(street)
                if(street.t==0):
                    continue

            if(total_time==0):
                continue
                
            ordered_streets_2 = sorted(ordered_streets, key=lambda x: x.t, reverse=True)

            curr_duration = math.ceil(float(total_time) / float(2))
            schedules.append(TrafficLightSchedule(intersection_id, ordered_streets_2, curr_duration))

        
        print(schedules)

        # get output

        redirect_str = str(len(schedules)) + "\n"
        """
        intersection
        N of incoming streets
        street1 street1_duration
        street2 street2_duration
        """
        for schedule in schedules:
            redirect_str += str(schedule.intersection) + "\n"
            redirect_str += str(len(schedule.streets)) + "\n"
            for street in schedule.streets:
                redirect_str += str(street.name) + " " + str(street.duration) + "\n"
        
        fm.write_file(f"/Output/{filex}.txt", redirect_str)
    #fm.write_file("/Output/demoOutput.txt", redirect_str)
    


if __name__== "__main__":
    main()