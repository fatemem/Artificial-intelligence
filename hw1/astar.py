import numpy as np
from heapq import *
cor=[(0,0)]
numofcity=0
finalcost=0

def heuristic(a, b):
    (x1, y1) = (float(a[0]),float(a[1]))
    (x2, y2) = (float(b[0]),float(b[1]))
    return abs(x1 - x2) + abs(y1 - y2)

def get_data(filename):
    global numofcity,cor
    f = open(filename, "r")
    lines = f.readlines()
    numofcity=lines[0]
    numofpath=lines[1]
    for line in lines[2:int(numofcity)+2]:
        c=line.split()
        cor.append((c[1],c[2]))
    route=np.zeros((int(numofcity)+1,int(numofcity)+1),dtype=float)
    for line in lines[int(numofcity)+2:]:
        c=line.split()
        route[int(c[0]),int(c[1])]=float(c[2])
    return route


def a_star_search(start, goal,route):
    global finalcost
    err="there is no way between 2 node"
    frontier = []
    heappush(frontier,(0, start))
    came_from = {}
    cost_so_far = {}
    came_from[int(start)] = None
    cost_so_far[int(start)] = 0

    while frontier:
        cur = heappop(frontier)
        current = int(cur[1])
        if current == int(goal):
            finalcost=cur[0]
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path

        for next in range(1, int(numofcity) + 1):
            if route[current][next] != 0:
                new_cost = cost_so_far[current] + route[current][next]
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    heappush(frontier,(new_cost + heuristic(cor[next],cor[int(goal)]), next))
                    came_from[next] = current

    return err


source = input("Enter source city: ")
destination = input("Enter destination city: ")
filedata=input("Enter name of your inputfile: ")
routes=get_data(filedata)
path=a_star_search(source,destination,routes)
print(path)
print("final cost:",finalcost)