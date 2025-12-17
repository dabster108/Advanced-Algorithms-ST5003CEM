import math

def dist(a, b):
    return math.dist(a, b)

def closest(points):
    if len(points) <= 3:
        return min(dist(points[i], points[j])
                   for i in range(len(points))
                   for j in range(i+1, len(points)))

    points.sort()
    mid = len(points) // 2
    left = points[:mid]
    right = points[mid:]

    d_left = closest(left)
    d_right = closest(right)    
    d = min(d_left, d_right)


    mid_x = points[mid][0]
    strip = [p for p in points if abs(p[0] - mid_x) < d]

    # Check at most a few points in strip
    strip.sort(key=lambda p: p[1])
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= d:
                break
            d = min(d, dist(strip[i], strip[j]))

    return d

pts = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("Closest distance:", closest(pts))
