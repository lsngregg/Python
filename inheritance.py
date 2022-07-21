"""

Create a class called Shape.

Define a method in it called what_am_i that prints "I am a shape" when called.

Change your Square and Rectangle classes from the previous challenges to inherit from Shape,
create Square and Rectangle objects, and call the new method on both of them.

"""

class Shape:
    def what_am_i():
         print("I am a shape")

class Square(Shape):
        def __init__(self, s1):
            self.s1 = s1

        def calculate_perimeter(self):
            perimeter = (self.s1 * 4)
            return perimeter


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        perimeter = (self.width * 2) + (self.length * 2)
        return perimeter 

square_1 = Square(10)
rectangle_1 =Rectangle(2,8)

square_1.what_am_i()
rectangle_1.what_am_i()



