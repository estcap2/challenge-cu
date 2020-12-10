#!/usr/bin/python
from __future__ import annotations
from point2d import Point2D
from mazeSolver import MazeSolver
import sys
MIN_PYTHON = (3, 1)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

input_maze = [
    ['A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'C', 'A', 'D', 'D', 'E', 'A', 'C', 'C', 'C', 'D', 'A'],
    ['A', 'C', 'C', 'D', 'A', 'E', 'A', 'D', 'A', 'D', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'E', 'D', 'D', 'A', 'D', 'E', 'A'],
    ['A', 'C', 'C', 'D', 'D', 'D', 'A', 'A', 'A', 'A', 'E', 'A'],
    ['A', 'C', 'A', 'A', 'A', 'A', 'A', 'D', 'D', 'D', 'E', 'A'],
    ['A', 'D', 'D', 'D', 'E', 'E', 'A', 'C', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'E', 'A', 'E', 'A', 'C', 'C', 'D', 'D', 'A'],
    ['A', 'D', 'E', 'E', 'A', 'D', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'D', 'A', 'A', 'D', 'A', 'C', 'D', 'D', 'A', 'A'],
    ['A', 'D', 'D', 'D', 'A', 'D', 'C', 'C', 'A', 'D', 'E', 'B'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
]

input_pattern = ['C', 'C', 'C', 'D', 'D', 'D', 'E', 'E', 'E', 'D', 'D', 'D']

input_finish = 'B'

# start manual input
input_start = Point2D(1, 0)

solver = MazeSolver(input_maze, input_pattern, input_start, input_finish)
solver.solve()
solver.print_dead_end_graphs()
solver.print_solutions_graphs()
print('\nExecution time [seconds] ' + str(solver.time))

# todo possible improvements:
""""
To be able to automatically get all start points, a list of possible start/end points should be implemented

For multiple starts, the comparison of success should be evaluated for position to check whether or not the two connected
points are already discovered
"""
