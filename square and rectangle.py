"""

Create Rectangle and Square classes.
Rectangle should have two instance variables: self.width and self.length.
Square should have one instance variable self.s1.

Define a method for both classes called calculate_perimeter 
    that calculates the perimeter of the shapes they represent and returns it.
    
Then, create Rectangle and Square objects and call the method on both of them.

"""
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        perimeter = (self.width * 2) + (self.length * 2)
        return perimeter 



class Square:
        def __init__(self, s1):
            self.s1 = s1

        def calculate_perimeter(self):
            perimeter = (self.s1 * 4)
            return perimeter


r1 = Rectangle(2,8)
s1 = Square(4)

r1.calculate_perimeter()
s1.calculate_perimeter()

class Obj1:
    def __init__(self):
        pass

class Obj2:
    def __init__(self):
        pass

def same(obj1, obj2):
    return obj1 is obj2