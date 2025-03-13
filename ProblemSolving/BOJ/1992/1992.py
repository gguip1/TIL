import sys

N = int(sys.stdin.readline().rstrip())
image = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def checkPoint(image, color):
    for _ in image:
        for pixel in _:
            if pixel != color:
                return False
    return True

def dac(image):
    if checkPoint(image, '0'):
        return '0'
    elif checkPoint(image, '1'):
        return '1'
    
    mid = len(image) // 2
    
    q1 = [_[:mid] for _ in image[:mid]]
    q2 = [_[mid:] for _ in image[:mid]]
    q3 = [_[:mid] for _ in image[mid:]]
    q4 = [_[mid:] for _ in image[mid:]]
    
    return '(' + dac(q1) + dac(q2) + dac(q3) + dac(q4) + ')'

print(dac(image))
