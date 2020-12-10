from point2d import Point2D
from mazePath import Path
import timeit


class MazeSolver:
    def __init__(self, maze, pattern, start: Point2D, finish):
        self._maze = maze
        self._pattern = pattern
        self._start = start
        self._finish = finish
        self._current_path = Path()
        self._current_path.append(start)
        self._paths_stack = []
        self._solutions = []
        self._dead_ends = []
        self._time = None

    @property
    def time(self):
        return self._time

    @property
    def solutions(self):
        return self._solutions

    @property
    def dead_ends(self):
        return self._dead_ends

    def print_solution_values(self, path):
        values = []
        for m in path:
            values.append(self._get_value(m))
        return values

    def print_solutions_graphs(self):
        for i, solution in enumerate(self._solutions):
            print('\nSolution ' + str(i + 1))
            print('\nPath ' + str(solution))
            self.print_path_graph(solution)

    def print_dead_end_graphs(self):
        for i, solution in enumerate(self._dead_ends):
            print('\nDead End ' + str(i + 1))
            self.print_path_graph(solution)

    def print_path_graph(self, path):
        # lowercase canvas
        canvas = [[value.lower() for value in row] for row in self._maze]

        # uppercase path
        for p in path:
            canvas[p.y][p.x] = canvas[p.y][p.x].upper()

        for idy, rows in enumerate(canvas):
            row = ""
            for idx, value in enumerate(rows):
                row = row + ' ' + value
            print(row)

    def solve(self, multiple_solutions: bool = False):
        # iteration to prevent recursion depth overflow
        start_time = timeit.default_timer()
        next_step = True
        while next_step:
            next_step = self._next_step(multiple_solutions)
        self._time = timeit.default_timer() - start_time
        return self

    def _next_step(self, multiple_solutions: bool = False):
        # verify solution
        if (len(self._current_path) > 1) & (self._current_value() == self._finish):
            self._solutions.append(self._current_path)
            if not multiple_solutions:
                return False
        else:
            # add all possible paths to stack.
            # should replace approach if much bigger mazes cause memory issues
            next_moves = self._next_moves()
            for m in next_moves:
                possible_path = Path(self._current_path)
                possible_path.append(m)
                self._paths_stack.append(possible_path)
            # dead ends. for debug purposes only
            if len(next_moves) == 0:
                self._dead_ends.append(self._current_path)

        # load from stack
        if len(self._paths_stack) > 0:
            self._current_path = self._paths_stack.pop()
            return True
        return False

    def _get_next_value(self):
        #TODO change to be able to start by ani point of pattern
        # using modulus to return next valid letter. useless if starting with offset
        return self._pattern[(len(self._current_path) - 1) % len(self._pattern)]

    def _get_value(self, point: Point2D):
        # get value or None if invalid position
        try:
            # map rows to y, columns to x
            return self._maze[point.y][point.x]
        except IndexError:
            return None

    def _current_location(self) -> Point2D:
        return self._current_path[-1]

    def _current_value(self):
        # get current value or None if invalid position
        return self._get_value(self._current_location())

    # return all valid possible values
    def _next_moves(self):
        # could be replaced by an elif chain
        possible_moves = [self._current_location().get_up(), self._current_location().get_down(),
                          self._current_location().get_left(), self._current_location().get_right()]

        moves = []
        for m in possible_moves:
            value = self._get_value(m)
            next_value = self._get_next_value()

            # inner validations separated for readability
            # not a valid maze location
            if value is None:
                continue

            # not a valid next value
            if (value != self._finish) and (value != next_value):
                continue

            # already visited
            if self._current_path.has_point(m):
                continue

            moves.append(m)
        return moves
