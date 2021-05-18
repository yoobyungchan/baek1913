t = int(input())

d = [[0]*t for _ in range(t)]

a = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x = y = t//2
#길이
k = 1
#방향
p = 0
num = 2
d[x][y] = 1
while True:
    for i in range(2):
        for j in range(k):
            x = x+dx[p]
            y = y+dy[p]
            d[x][y] = num
            if num == t * t:
                break
            num += 1
        p += 1
        p %= 4
        if num == t * t:
            break
    k += 1
    if num == t*t:
        break

m = n = 0
for i in range(t):
    for j in range(t):
        if d[i][j] == a:
            m = i+1
            n = j+1
        print(d[i][j], end=' ')
    print()
print(m, n)



