#!/usr/bin/pthon3
"""Module: Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.height))
