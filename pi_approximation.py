import random

def approximate_pi(n):
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= 1:
            count += 1
        
    # count is the number of points inside the unit circle in the first quadrant,
    # n is the number of points in the unit square in the first quadrant,
    # count/n is approximately the area of the unit circle in the first quadrant,
    # which is pi * r^2 /4 = pi/4, because the radius of the unit circle is 1.

    return 4 * count / n