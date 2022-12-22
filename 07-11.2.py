import math                                         

class Circle:                                       
    def __init__(self, r):                          
        self.r = r                                  
    
    def get_circumference(self):                    
        return round(2 * math.pi * self.r, 2)           

    def get_ploshad(self):                           
        return round(math.pi *(self.r ** 2))              

circle = Circle(5)
print(circle.get_circumference())
print(circle.get_ploshad())