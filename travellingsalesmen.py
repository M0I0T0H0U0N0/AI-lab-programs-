import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def nearestneighbour(points):
    n = len(points)
    unvisited = set(range(n))
    tour = [0]
    unvisited.remove(0)
    
    while unvisited:
        currentpoint = tour[-1]
        nearestpoint = min(unvisited, key=lambda x: distance(points[currentpoint], points[x]))
        tour.append(nearestpoint)
        unvisited.remove(nearestpoint)
    
    tour.append(tour[0])
    
    return tour    

if __name__ == "__main__":
    points = [(0,0), (1,2), (2,3), (3,4), (4,2)]
    tour = nearestneighbour(points)
    print("Optimal tour:", tour)
