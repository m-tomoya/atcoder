while(True):
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        low = ""
        if i % 2 == 0:
            for k in range(w):
                if k % 2 == 0:
                    low.append("#")
                else:
                    low.append(".")
        else:
            for k in range(w):
                if k % 2 == 0:
                    low.append(".")
                else:
                    low.append("#")
        print(low)
    pritn()
