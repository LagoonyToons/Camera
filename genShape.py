def generateOctagon(x, y, s):
    pointA = [x+(s*.5),y+s]
    pointB = [x+(s),y+(s*.5)]
    pointD = [x+(s*.5),y-s]
    pointC = [x+(s),y-(s*.5)]
    pointE = [x-(s*.5),y-s]
    pointF = [x-(s),y-(s*.5)]
    pointH = [x-(s*.5),y+s]
    pointG = [x-(s),y+(s*.5)]
    pointList = [pointA, pointB, pointC, pointD, pointE, pointF, pointG, pointH]
    return pointList
def generateTriangle(x, y, s):
    pointA = [x-s, y]
    pointB = [x, y-s*2]
    pointC = [x+s, y]
    pointList = [pointA, pointB, pointC]
    return pointList