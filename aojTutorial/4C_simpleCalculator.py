while(True):
    x, op, y = input().split()
    a = int(x)
    b = int(y)
    if op == "+":
        print(a+b)
    if op == "-":
        print(a-b)
    if op == "*":
        print(a*b)
    if op == "/":
        print(a//b)
    if op == "?":
        break
