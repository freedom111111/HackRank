from itertools import combinations
from functools import reduce
import math

A = [0,1]
B = [2,3]
C = [1,0]
points =[A,B,C]

def area(points):
    x1,y1 = points[0]
    x2,y2 = points[1]
    x3,y3 = points[2]
    return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2

def int_points_in_triangle(points):
    res = []
    x = []
    y = []
    for i in range(3):
        x.append(points[i][0])
        y.append(points[i][1])
    total = area(points)
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)
    for x in range(x_min,x_max+1):
        for y in range(y_min,y_max+1):
            sum = 0
            for c in combinations(points,2):
                sum += area([[x,y]]+list(c))
            if sum == total:
                res.append([x,y])
    return res
def cloest_point(points,res): 
    dis = {}
    for p in res:
        distance = [math.sqrt((p[0]-points[i][0])**2+(p[1]-points[i][1])**2) for i in range(3)]
        sum = reduce(lambda x,y: x+y, distance)
#        print(distance)
#        print(sum)
        dis[(p[0],p[1])] = round(sum,4)
#        print(dis)
    return min(dis, key=dis.get), min(dis.values())
    
res = int_points_in_triangle(points)
print(res)
ans, distance = cloest_point(points,res)
print('The nearest point is',ans)
print('The nearest distance is',distance)
