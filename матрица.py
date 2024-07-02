#-----1--2--3--4--5--6--7--8--9--10
A = [[0, 2, 3, 5, 0, 0, 0, 0, 0, 0],
     [2, 0, 0, 0, 4, 0, 0, 0, 0, 0],
     [3, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [5, 0, 0, 0, 2, 3, 0, 1, 0, 0],
     [0, 4, 0, 2, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 3, 0, 0, 2, 0, 6, 4],
     [0, 0, 1, 0, 0, 2, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 6, 0, 1, 0, 7],
     [0, 0, 0, 0, 0, 4, 0, 0, 7, 0]]

m = 10
#-----------------------------------

d=[]
for i in range(m):
    d.append([0])
    for j in range (m-1):
        d[i].append(0)

for i in range(m):
    for j in range (m):
        d[i][j] = A[i][j]
        if A[i][j] == 0 and i != j:
            d[i][j] = 1000

print("matrix d0")
for i in range (m):
    print(d[i])

print()

for k in range (m):
    for i in range (m):
        for j in range (m):
            d[i][j] = min(d[i][j], d[i][j] + d[k][j])

print("matrix d")
for i in range (m):
    print(d[i])
