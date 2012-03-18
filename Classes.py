
#####################################################################
#Used to perform various functions on sets of coordinates
class Vector(object):
    #Finds the x and y distance between two coordinates
    def __init__(self, current, target):
        self.diff = (target[0] - current[0], target[1] - current[1]
                     
    #Returns diagonal distance between two coordinates
    def distance(self):
        self.a = self.diff[0]
        self.b = self.diff[1]
        return math.sqrt(self.a**2 + self.b**2)

    #Returns the distance x any y as if the direct distance was 1
    def unit(self):
        distance = self.distance()
        self.a_unit = self.a/distance
        self.b_unit = self.b/distance
        return self.a_unit, self.b_unit

    #Returns sum of two vectors
    def add(self, first, second):
        self.sum = (first[0] + second [0], first[1] + second [1])
        return self.sum

    #Returns product of a vector and a number
    def multiply(self, v, multi):
        self.product = (v[0]*multi, v[1]*multi)
        return self.product
#####################################################################


class Unit(object):
    def position(self):
        self.coordinates -
