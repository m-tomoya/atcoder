while(True):
    n = int(input())
    if n == 0:
        break
    scores = list(map(int, input().split()))
    m = sum(scores)/n
    var_sum = 0
    for i in range(n):
        var_sum += (scores[i]-m)**2
    print((var_sum/n)**0.5)
