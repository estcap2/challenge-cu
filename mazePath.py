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
        """Overrides the default implementation ( __ne__ unnecessary in Python 3)"""
        if isinstance(other, Path):
            return len(other._points) == len(self._points) and sorted(other._points) == sorted(self._points)
        return False

    def append(self, point: Point2D):
        self._points.append(point)

    def get_point(self, index: int):
        return self._points[index]

    def has_point(self, point: Point2D):
        for m in self._points:
            if m == point:
                return True
        return False
