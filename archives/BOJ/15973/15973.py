import sys
input = sys.stdin.readline

p_x1, p_y1, p_x2, p_y2 = map(int, input().strip().split())
q_x1, q_y1, q_x2, q_y2 = map(int, input().strip().split())

def check_null():
    return (p_x2 < q_x1 or 
            q_x2 < p_x1 or 
            p_y2 < q_y1 or 
            q_y2 < p_y1)

def check_point():
    return ((p_x2 == q_x1 and p_y2 == q_y1) or
            (p_x1 == q_x2 and p_y1 == q_y2) or
            (p_x2 == q_x1 and p_y1 == q_y2) or
            (p_x1 == q_x2 and p_y2 == q_y1))

def check_line():
    return ((p_x1 == q_x2 and (p_y1 <= q_y1 < p_y2 or p_y1 < q_y2 <= p_y2 or q_y1 <= p_y1 < q_y2 or q_y1 < p_y2 <= q_y2)) or 
            (p_x2 == q_x1 and (p_y1 <= q_y1 < p_y2 or p_y1 < q_y2 <= p_y2 or q_y1 <= p_y1 < q_y2 or q_y1 < p_y2 <= q_y2)) or 
            (p_y1 == q_y2 and (p_x1 <= q_x1 < p_x2 or p_x1 < q_x2 <= p_x2 or q_x1 <= p_x1 < q_x2 or q_x1 < p_x2 <= q_x2)) or 
            (p_y2 == q_y1 and (p_x1 <= q_x1 < p_x2 or p_x1 < q_x2 <= p_x2 or q_x1 <= p_x1 < q_x2 or q_x1 < p_x2 <= q_x2)))

if check_null():
    print('NULL')
elif check_point():
    print('POINT')
elif check_line():
    print('LINE')
else:
    print('FACE')
