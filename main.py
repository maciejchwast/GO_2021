import random
import math


class Point:

    def __init__(self, px, py):
        self.x = px
        self.y = py

    def print(self):
        return "X = "+str(round(self.x, 2))+", Y = "+str(round(self.y, 2))


class Straight:

    def __init__(self, p1: Point, p2: Point):
        self.a = (p1.y - p2.y) / (p1.x - p2.x)
        self.b = p1.y - self.a * p1.x


class Line:
    head: Point
    tail: Point

    def print(self):
        return "head point: "+self.head.print()+" tail point: "+self.tail.print()

    def __init__(self, p1: Point, p2: Point):
        self.head = p1
        self.tail = p2
        self.belongs_to_straight = Straight(p1, p2)


def pointsToLine(p1: Point, p2: Point):
    a = (p1.y - p2.y)/(p1.x - p2.x)
    b = p1.y - a * p1.x
    print("Points "+p1.print()+" and "+p2.print()+" are creating y="+str(round(a, 2))+"x+"+str(round(b, 2)))
    return Line(p1, p2)


def randomPoint():
    a = random.randrange(-100, 100)
    b = random.randrange(-100, 100)
    return Point(a, b)


def belongsToLine(p: Point, l: Line):
    if p.x * l.belongs_to_straight.a + l.belongs_to_straight.b == p.y:
        return True
    else:
        return False


def belongsToStraight(p: Point, s: Straight):
    if p.x * s.a + s.b == p.y:
        return True
    else:
        return False


def translateLine(v: Point, l: Line):
    return Line(Point(l.head.x + v.x, l.head.y + v.y), Point(l.tail.x + v.x, l.tail.y + v.y))


def rotateLine(rad, l: Line):
    newX = (l.head.x - l.tail.x) * math.cos(rad) - (l.head.y - l.tail.y) * math.sin(rad) + l.tail.x
    newY = (l.head.x - l.tail.x) * math.sin(rad) - (l.head.y - l.tail.y) * math.cos(rad) + l.tail.y
    return Line(l.head, Point(newX, newY))


def mirrorPoint(axe, p: Point):
    if axe == 'x':
        return Point(-p.x, p.y)
    if axe == 'y':
        return Point(p.x, -p.y)


if __name__ == '__main__':
    Pnt1 = randomPoint()
    Pnt2 = randomPoint()
    Pnt3 = randomPoint()
    print("Random points: ", Pnt1.print(), " ", Pnt2.print(), " ", Pnt3.print())
    line1 = pointsToLine(Pnt1, Pnt2)
    print("Does point 3 belong to straight created by points 1 and 2? ", belongsToLine(Pnt3, line1))
    vect = randomPoint()
    line1 = translateLine(vect, line1)
    print("Line 1 was transformed by random vector: ", vect.print(), " and now it has coordinates: ", line1.print())
    print("Line 1 was rotated by 10 radians. Now its coordinates are ", rotateLine(10, line1).print())
    print("Point 1 before mirror against OX: ", Pnt1.print(), " and after: ", mirrorPoint('x', Pnt1).print())
    print("Point 2 before mirror against OY: ", Pnt2.print(), " and after: ", mirrorPoint('y', Pnt2).print())
