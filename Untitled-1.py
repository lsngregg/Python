"""
Create a Square class that has one method that calculates its perimeter.
 When you print a Square object, a message should print telling you the length
     of each of the four sides of the shape.
     
     For example, the code 
        print(Square(29)) 
        
        should print "29 by 29 by 29 by 29".

"""

class Square:
        def __init__(self, s1):
            self.s1 = s1

        def calculate_perimeter(self):
            perimeter = (self.s1 * 4)
            return perimeter