class Line(object):
    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

    def intersects(self, other_line):
        epsilon = .000001
        delta_slope = abs(self.slope - other_line.slope)
        delta_intercept = abs(self.intercept - other_line.intercept)
        return delta_slope > epsilon or delta_intercept < epsilon

if __name__ == '__main__':
    l1 = Line(1, 5)
    l2 = Line(1.0000000000001, 5)
    l3 = Line(1, 6)
    assert l1.intersects(l2)
    assert l2.intersects(l1)
    assert not l1.intersects(l3)
    assert not l2.intersects(l3)