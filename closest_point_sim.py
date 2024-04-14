import numpy as np

def point_in_circle(k, p, q):
    """
    Generate k random points in the circle (x-p)^2 + (y-q)^2 < 1
    """
    L = []
    points = []
    while len(L) < k:
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            L.append(np.sqrt((x-p)**2 + (y-q)**2))
            points.append((x, y))
    L.sort()
    return L, points

def closest_point_circle(darts, trials, p, q):
    """
    Return the average distance of the closest point to the center of the circle
    """
    L = []
    for i in range(trials):
        L.append(min(point_in_circle(darts, p, q)[0]))
    return np.mean(L)

def points_in_ellipse(k, a, b):
    """
    Generate k random points in the ellipse x^2/a^2 + y^2/b^2 < 1
    """
    L = []
    points = []
    while len(L) < k:
        x = np.random.uniform(-a, a)
        y = np.random.uniform(-b, b)
        if x**2/a**2 + y**2/b**2 < 1:
            L.append(np.sqrt(x**2 + y**2))
            points.append((x, y))
    L.sort()
    return L, points

def closest_point_ellipse(darts, trials):
    """
    Return the average distance of the closest point to the center of the ellipse
    """
    L = []
    for i in range(trials):
        L.append(min(point_in_ellipse(darts, 0.5, 0.5)[0]))
    return np.mean(L)


def main():
    # Let q = 0. Vary p from 0 to 1 and plot the average distance of the closest point to the center of the circle
    import matplotlib.pyplot as plt
    p = np.linspace(0, 1, 100)
    avg_dist = [closest_point_circle(1000, 1000, i, 0) for i in p]
    plt.plot(p, avg_dist)
    plt.xlabel('p')
    plt.ylabel('Average distance of the closest point to the center of the circle')
    plt.show()

if __name__ == '__main__':
    main()

