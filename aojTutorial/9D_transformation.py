text = input()
q = int(input())
for _ in range(q):
    order = input().split()
    a, b = map(int, order[1:3])
    if order[0] == "replace":
        word = order[3]
        text = text[:a] + word + text[b+1:]
    if order[0] == "reverse":
        r_word = text[a:b+1][::-1]
        text = text[:a] + r_word + text[b+1:]
    if order[0] == "print":
        print(text[a:b+1])
