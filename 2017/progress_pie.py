import math

radius = 50
currentRadSq = 0

def isInCircle(x, y):
    # boundry sample : 2(x-50)**2 = 50**2
    # x = 85.5355...
    if currentRadSq < 50**2:
        return True
    else:
        return False

def isSmallerAngle(target, x, y):
    target = target / 100 * 360
    if x >= 50 and y > 50:
        # zone ++
        # print('++')
        r = math.sqrt(currentRadSq)
        rad = math.asin((x - 50)/r)
        degree = math.degrees(rad)
        return degree < target
    elif x > 50 and y <= 50:
        # zone +-
        # print('+-')
        r = math.sqrt(currentRadSq)
        rad = math.asin((x - 50)/r)
        degree = math.degrees(rad) + 90
        return degree < target
    elif x <= 50 and y < 50:
        # zone --
        # print('--')
        r = math.sqrt(currentRadSq)
        rad = math.asin((50 - x)/r)
        degree = math.degrees(rad) + 180
        return degree < target
    elif x < 50 and y >= 50:
        # zone -+
        # print('-+')
        r = math.sqrt(currentRadSq)
        rad = math.asin((50 - x)/r)
        degree = math.degrees(rad) + 270
        return degree < target
    else:
        #50,50
        if target == 0:
            return False
        else:
            return True

# print(isInCircle(85,85))
# print(math.sqrt(50))
# print(isSmallerAngle(0,55,55))
# print(isSmallerAngle(12,55,55))
# print(isSmallerAngle(13,55,55))
# print(isSmallerAngle(87,20,40))

# axis
# print(isSmallerAngle(1,50,51))
# print(isSmallerAngle(90,51,50))
# print(isSmallerAngle(180,50,49))
# print(isSmallerAngle(270,49,50))

t = int(input())
lines = [];
for i in range(t):
    p, x, y = map(int, input().split())
    currentRadSq = (x-radius)**2 + (y-radius)**2
    if isInCircle(x, y) and isSmallerAngle(p, x, y):
        lines.append('Case #%d: black' % (i+1))
    else:
        lines.append('Case #%d: white' % (i+1))

for i in range(len(lines)):
    print(lines[i])
