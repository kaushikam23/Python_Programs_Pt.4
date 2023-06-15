class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, other):
        if isinstance(other, Point):
            nx = self.x + other.x
            ny = self.y + other.y
        elif isinstance(other, tuple) and len(other) == 2:
            nx = self.x + other[0]
            ny = self.y + other[1]
        else:
            raise ValueError("Invalid operand")

        return Point(nx, ny)

p1 = Point(2, 3)
p2 = Point(5, 7)


p3 = p1.add(p2)
print("p3 coordinates: ", "(",p3.x,p3.y,")")  


p4 = p1.add((1, 2))
print("p4 coordinates: ","(", p4.x,p4.y,")")  
