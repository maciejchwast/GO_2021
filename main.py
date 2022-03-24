import random
import math
import numpy as np
import matplotlib.pyplot as plt


class Point:

    def __init__(self, px, py):
        self.x = px
        self.y = py

    def print(self):
        return "X = "+str(round(self.x, 2))+", Y = "+str(round(self.y, 2))


class Straight:

    def print(self):
        return "y = "+str(round(self.a,2))+"X + "+str(round(self.b,2))

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


class Triangle:
    tip1: Point
    tip2: Point
    tip3: Point

    side1: Straight
    side2: Straight
    side3: Straight

    def __init__(self,p1: Point,p2: Point, p3:Point):
        self.tip1 = p1
        self.tip2 = p2
        self.tip3 = p3
        self.side1 = Straight(self.tip1, self.tip2)
        self.side2 = Straight(self.tip2, self.tip3)
        self.side3 = Straight(self.tip3, self.tip1)

    def draw(self):
        plt.plot([self.tip1.x,self.tip2.x],[self.tip1.y, self.tip2.y])
        plt.plot([self.tip2.x,self.tip3.x],[self.tip2.y, self.tip3.y])
        plt.plot([self.tip3.x,self.tip1.x],[self.tip3.y, self.tip1.y])
        plt.show()

    def is_point_inside(self, p: Point):
        plt.plot(p.x, p.y, 'o')
        self.draw()
        conditions = ["x","x","x"]
        conditions[0] = whichSide(self.side1, p)
        conditions[1] = whichSide(self.side2, p)
        conditions[2] = whichSide(self.side3, p)
        conditions.sort()
        if conditions[0] == 'above' and conditions[1] == 'below' and conditions[2] == 'below':
            return True
        else:
            return False


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


def slopeToStandardLinearEquation(s: Straight):
    a = s.a
    b = 1
    c = -s.b
    return [a, b, c]


def whichSide(s: Straight, p: Point):
    if s.a * p.x + s.b < p.y:
        return 'above'
    elif s.a * p.x + s.b > p.y:
        return 'below'
    else:
        return 'on'


def pointsToLineTab(p1: Point, p2: Point):
    a = (p1.y - p2.y) / (p1.x - p2.x)
    b = p1.y - a * p1.x
    return [a, b]


def crossingPointCramer(t1, t2):
    W = t1[0]*t2[1] - t2[0]*t1[1]
    Wx = -t1[2]*t2[1] - (-t2[2]*t1[1])
    Wy = t1[0]*(-t2[2]) - t2[0]*(-t1[2])

    x = Wx/W
    y = Wy/W

    return Point(x, y)


def crossingPointLines(l1: Line, l2: Line):
    s1 = l1.belongs_to_straight
    s2 = l2.belongs_to_straight
    return crossingPointCramer(slopeToStandardLinearEquation(s1), slopeToStandardLinearEquation(s2))

def calculateTriangleArea(p1: Point, p2: Point, p3:Point):
    tmp1 = p2.x - p1.x
    tmp2 = p3.y - p1.y
    tmp3 = p3.x - p1.x
    tmp4 = p2.y - p1.y
    return 0.5 * ((tmp1*tmp2) - (tmp3*tmp4))

def lab1_and_2():
    print("Random points: ", Pnt1.print(), " ", Pnt2.print(), " ", Pnt3.print())
    line1 = pointsToLine(Pnt1, Pnt2)
    print("Does point 3 belong to straight created by points 1 and 2? ", belongsToLine(Pnt3, line1))
    vect = randomPoint()
    line1 = translateLine(vect, line1)
    print("Line 1 was transformed by random vector: ", vect.print(), " and now it has coordinates: ", line1.print())
    print("Line 1 was rotated by 10 radians. Now its coordinates are ", rotateLine(10, line1).print())
    print("Point 1 before mirror against OX: ", Pnt1.print(), " and after: ", mirrorPoint('x', Pnt1).print())
    print("Point 2 before mirror against OY: ", Pnt2.print(), " and after: ", mirrorPoint('y', Pnt2).print())
    line2 = pointsToLine(Pnt3, Pnt2)
    print("Line 1 is ", line1.belongs_to_straight.print())
    print("Line 2 is ", line2.belongs_to_straight.print())
    print("Lines 1 and 2 are crossing at ", crossingPointLines(line1, line2).print())
    print("Points 1 2 and 3 are: 1: ", Pnt1.print(), " 2: ", Pnt2.print(), " 3: ", Pnt3.print())
    print("Area of triangle made from points 1 2 and 3 is ", str(round(calculateTriangleArea(Pnt1, Pnt2, Pnt3), 2)))

if __name__ == '__main__':
    Pnt1 = randomPoint()
    Pnt2 = randomPoint()
    Pnt3 = randomPoint()
    Pnt4 = randomPoint()
    #lab1_and_2()
    #plt.plot([Pnt1.x, Pnt2.x], [Pnt1.y, Pnt2.y])
    #plt.plot(Pnt3.x, Pnt3.y,'o')
    #plt.show()
    #print("The point is "+whichSide(Straight(Pnt1,Pnt2),Pnt3)+" line")
    t1 = Triangle(Pnt1, Pnt2, Pnt3)
    t1.draw()
    print(t1.is_point_inside(Pnt4))
