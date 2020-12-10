class Point2D:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def __eq__(self, other):
        """Overrides the default implementation ( __ne__ unnecessary in Python 3)"""
        if isinstance(other, Point2D):
            return (self.x == other.x) & (self.y == other.y)
        return False

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    def get_up(self) -> 'Point2D':
        return Point2D(self.x, self.y - 1)

    def get_down(self) -> 'Point2D':
        return Point2D(self.x, self.y + 1)

    def get_left(self) -> 'Point2D':
        return Point2D(self.x - 1, self.y)

    def get_right(self) -> 'Point2D':
        return Point2D(self.x + 1, self.y)
