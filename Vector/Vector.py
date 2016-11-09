from math import sqrt


class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if self(len)==other(len):
            return self+other
        else:
             return 'error'




    def magnitude(self,components):

    # Write a function that adds the squares of the components
    # and returns the square root of the sum (like the pythagorean theorem)

    def dot(self, other):

    # if self and other are the same length,
    # return the sum of the products of each component
    # otherwise return an error
    # example: if self is the vector [1, 2, 3] and other is [4, 5, 6],
    # dot(self, other) should return (1 * 4) + (2 * 5) + (3 * 6),
    # the NUMBER 32. This shouldn't be a vector!







