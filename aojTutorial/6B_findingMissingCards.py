n = int(input())
sl = []
hl = []
cl = []
dl = []
for i in range(n):
    s, r = map(str, input().split())
    if s == "S":
        sl.append(int(r))
    if s == "H":
        hl.append(int(r))
    if s == "C":
        cl.append(int(r))
    if s == "D":
        dl.append(int(r))
sl.sort()
hl.sort()
cl.sort()
dl.sort()
for i in range(1, 14):
    if i not in sl:
        print("S", i)
for i in range(1, 14):
    if i not in hl:
        print("H", i)
for i in range(1, 14):
    if i not in cl:
        print("C", i)
for i in range(1, 14):
    if i not in dl:
        print("D", i)
