from unittest import expectedFailure, removeResult

import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[5, 6, 7], [8, 9], [10, 11], []]
        result = lab4.first_element(input)
        expected = [5, 8, 10]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates_1(self):
        input = [data.Point(2, 3), data.Point(4, 6), data.Point(10, 100)]
        result = lab4.x_coordinates(input)
        expected = [2, 4, 10]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input = [data.Point(52, 31), data.Point(64, 63), data.Point(0, 5)]
        result = lab4.x_coordinates(input)
        expected = [52, 64, 0]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        input = [data.Point(1.0, 2.0), data.Point(-2.0, 3.5)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [1.0, 2.0]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        input = [data.Point(15, -4.0), data.Point(-67.0, -3443)]
        result = lab4.are_in_positive_quadrant(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 4
    def test_distance_1(self):
        input1 = data.Point(0, 0)
        input2 = data.Point(3, 4)
        result = lab4.distance(input1, input2)
        expected = 5.00
        self.assertEqual(expected, result)

    def test_distance_2(self):
        input1 = data.Point(5,10)
        input2 = data.Point(10,22)
        result = lab4.distance(input1, input2)
        expected = 13.00
        self.assertEqual(expected, result)

    # Part 5
    def test_manhattan_distance_1(self):
        input1 = data.Point(2, 5)
        input2 = data.Point(7, 10)
        result = lab4.manhattan_distance(input1, input2)
        expected = 10.0
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        input1 = data.Point(100, 500)
        input2 = data.Point(1, 25)
        result = lab4.manhattan_distance(input1, input2)
        expected = 574.0
        self.assertEqual(expected, result)

    # Part 6
    def test_distance_all_1(self):
        input1 = [data.Point(1, 1), data.Point(7, 24)]
        result = lab4.distance_all(input1)
        expected = [1.41, 25.00]
        self.assertEqual(expected, result)

    def test_distance_all_2(self):
        input1 = [data.Point(-3, -4), data.Point(9, 40)]
        result = lab4.distance_all(input1)
        expected = [5.00, 41.00]
        self.assertEqual(expected, result)




#if __name__ == '__main__':
 #   unittest.main()
