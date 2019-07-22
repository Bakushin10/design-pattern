class Building(object):
    def __init__(self):
        self.build_floor()
        self.build_size()
        self.build_yard()
    
    def build_floor(self):
        raise NotImplementedError
    
    def build_size(self):
        return NotImplementedError
    
    def build_yard(self):
        return NotImplementedError
        
    
    def __repr__(self):
        return 'Floor: {0.floor} | Size : {0.size}'.format(self)

class House(Building):
    def build_floor(self):
        self.floor = 'One'
    
    def build_size(self):
        self.size = 'Big'
    
    def build_yaed(self):
        self.yard = "12"
    
class Flat(Building):
    def build_floor(self):
        self.floor = 'More than One'
    
    def build_size(self):
        self.size = 'Small'

    def build_yaed(self):
        self.yard = "12"

class ComplexBuilding(object):
    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)

def construc_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building
 
if __name__ == "__main__":
    house = House()
    print(house)

    flat = Flat()
    print(flat)

    b = Building()

    
