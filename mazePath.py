from point2d import Point2D


class Path:
    # could inherit from list class
    class PathIterator:
        def __init__(self, path: 'Path'):
            self._path = path
            self._index = 0

        def __next__(self):
            if self._index < len(self._path):
                result = self._path.get_point(self._index)
                self._index += 1
                return result
            raise StopIteration

    def __init__(self, iterable=None):
        self._points = []
        if iterable:
            for item in iterable:
                self.append(item)

    def __len__(self):
        return len(self._points)

    def __iter__(self):
        return Path.PathIterator(self)

    def __getitem__(self, floor_number):
        return self._points[floor_number]

    def __eq__(self, other):
        """Overrides the default = operator implementation"""
        if isinstance(other, Path):
            return len(other._points) == len(self._points) and sorted(other._points) == sorted(self._points)
        return False

    def __str__(self):
        """Overrides the default to string implementation"""
        s = '['
        first = True
        for p in self._points:
            if first:
                first = False
            else:
                s += ', '
            s += str(p)
        s += ']'
        return s

    def append(self, point: Point2D):
        self._points.append(point)

    # retrives Point2D at index
    def get_point(self, index: int) -> Point2D:
        return self._points[index]

    # checks whether the point is already present in Path
    def has_point(self, point: Point2D) -> bool:
        for m in self._points:
            if m == point:
                return True
        return False
