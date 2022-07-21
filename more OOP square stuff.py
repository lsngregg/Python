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
            perimeter = (s1 * 4)
            return perimeter
            
        def change_size(self, x):
            self.s1 += x


s1 = Square(8)

r1 = Rectangle(2, 4)