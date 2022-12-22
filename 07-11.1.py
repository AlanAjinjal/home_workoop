#Написать класссы треугольника и круга, как мы писали класс прямоугольника на паре.
#Треугольник: (аттрибуты: три стороны, методы: площадь и периметр). Круг: (аттрибуты: радиус, методы: длина окружности и площадь). 

import math                                                         

class Triangle:                                                    
    def __init__(self, a ,b, c):                                    
        self.a = a                                                  
        self.b = b                                                  
        self.c = c                                                  

    def get_perimeter(self):                                        
        return round((self.a + self.b + self.c), 2)                             

    def get_ploshad(self):                                              
        p = (self.a + self.b + self.c) / 2                              
        return round(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)

triangle = Triangle(3, 4, 5)
print(triangle.get_perimeter())
print(triangle.get_ploshad())