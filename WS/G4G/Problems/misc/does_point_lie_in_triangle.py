# coding=utf-8
"""
amzn

http://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/

Let the coordinates of three corners be (x1, y1), (x2, y2) and (x3, y3).
And coordinates of the given point P be (x, y)

1) Calculate area of the given triangle, i.e., area of the triangle ABC in the above diagram. Area A = [ x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2)]/2
2) Calculate area of the triangle PAB. We can use the same formula for this. Let this area be A1.
3) Calculate area of the triangle PBC. Let this area be A2.
4) Calculate area of the triangle PAC. Let this area be A3.
5) If P lies inside the triangle, then A1 + A2 + A3 must be equal to A.
"""


def area(c1, c2, c3):
    x1 = c1[0]
    y1 = c1[1]
    x2 = c2[0]
    y2 = c2[1]
    x3 = c3[0]
    y3 = c3[1]

    _area = ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))) / 2.0

    return _area


def is_in_triangle(a, b, c, x):
    xab = area(a, b, x)
    xbc = area(b, c, x)
    xac = area(a, c, x)
    abc = area(a, b, c)

    return xab + xbc + xac == abc
