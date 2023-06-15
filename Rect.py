class Rectangle:
    def __init__(self, corner, width,height):
        self.corner = corner
        self.width = width
        self.height = height
       

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x += dx
    rectangle.corner.y += dy


corner_point = Point(2, 3)
rectangle = Rectangle(corner_point, 10, 5)

print("Before moving:")
print("Rectangle corner coordinates: ", rectangle.corner.x, rectangle.corner.y)


move_rectangle(rectangle, 3, 2)

print("After moving:")
print("Rectangle corner coordinates: ",rectangle.corner.x,rectangle.corner.y)  
