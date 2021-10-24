import sys

n, m = int(input().split())

start_point_x = n
start_point_y = 0

cnt = 1

if n >= m:
    while(True):
        if start_point_x - 2 => 0 and start_point_y + 1 <= m:
            start_point_x -= 2
            start_point_y += 1
            cnt += 1
        elif start_point_x + 2 =< n and start_point_y + 1 <= m:
            start_point_x += 2
            start_point_y += 1
            cnt += 1
        elif start_point_x - 1 => 0 and start_point_y + 2 <= m:
            start_point_x -= 1
            start_point_y += 2
            cnt += 1
        elif start_point_x  + 1 =< n  and start_point_y <= m - 2:
            start_point_x -= 1
            start_point_y += 2
            cnt += 1

else :
