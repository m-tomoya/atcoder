while(True):
    word = input()
    if word == "-":
        break
    m = int(input())
    for i in range(m):
        sh = int(input())
        latter = word[sh:]
        former = word[:sh]
        word = latter + former
    print(word)
