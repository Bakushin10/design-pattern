import math

# values will be updated 
class Circle:

    """Circle with radius, area, and diameter."""

    def __init__(self, radius=1):
        self.radius = radius

    # def __repr__(self):
    #     return f'Circle({self.radius})'


    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

# values wont be updated 
class Circle2:
    def __init__(self, radius = 1):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
    
    @property
    def area(self):
        return math.pi * self._radius ** 2
    
    
    @property
    def diameter(self):
        return self._radius * 2

# values wont be updated 
class Circle3:
    def __init__(self, radius = 1):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
    
    @property
    def area(self):
       return math.pi * self._radius ** 2
    
    @property
    def diameter(self):
        return self._radius * 2

class Geeks: 
     def __init__(self): 
          self._age = 0
       
     # using property decorator 
     # a getter function 
     @property
     def age(self): 
         print("getter method called") 
         return self._age 
       
     # a setter function 
     @age.setter 
     def age(self, a): 
         if a < 18: 
            raise ValueError("Sorry you age is below eligibility criteria") 
         print("setter method called") 
         self._age = a 
         
# c = Circle3()

# print(c.radius)
# print(c.area)
# c.radius = -1
# print(c.radius)
# print(c.diameter)

mark = Geeks() 
mark.age = 17
print(mark.age)