n = int(input())
xlist = list(map(int, input().split()))
ylist = list(map(int, input().split()))

for p in range(1, 4):
    print("{0:.6}".format(
        sum([abs(a-b)**p for a, b in zip(xlist, ylist)]**(1/p))))
print("{0:.6f}".format(max([abs(a-b) for a, b in zip(xlist, ylist)])))
