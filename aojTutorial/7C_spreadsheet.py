r, c = map(int, input().split())
list = [list(map(int, input().split())) for _ in range(r)]
lastlist = [0 for _ in range(c+1)]

for i in range(r):
    list[i].append(sum(list[i]))
    for j in range(c+1):
        lastlist[j] += list[i][j]
    print(*list[i])
print(*lastlist)
