import data
from data import Point
import math

# Write your functions for each part in the space below.

# Part 1
def first_element(list1:list[list[int]])->list:
    new_list = []
    for first in list1:
        if first != []:
            new_list.append(first[0])
    return new_list

# Part 2
def x_coordinates(list2: list[Point])->list:
    xlist = []
    for point in list2:
        xlist.append(point.x)
    return xlist

# Part 3
def are_in_positive_quadrant(list3: list[Point])->list:
    pos_vals = []
    for val in list3:
        if val.x >= 0 and val.y >= 0:
            pos_vals.append(val.x)
            pos_vals.append(val.y)
    return pos_vals

# Part 4
def distance(point1 : Point, point2 : Point)->float:
    return round(math.sqrt((point1.x - point2.x)**2 + ((point1.y - point2.y)**2)), 2)

# Part 5
def manhattan_distance(pt1: Point, pt2: Point)->float:
    return round(abs(pt1.x-pt2.x) + abs(pt1.y - pt2.y))

# Part 6
def distance_all(list4: list[Point])->list[float]:
    origin = data.Point(0,0)
    list4 = [distance(origin, list4[idx]) for idx in range(len(list4))]
    return list4