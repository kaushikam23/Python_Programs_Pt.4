import math

class P_D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def distance(point1, point2):
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    return distance

p1 = P_D(2, 3)
p2 = P_D(5, 7)
dist = distance(p1, p2)
print("The distance between p1 and p2 is: ", dist)
