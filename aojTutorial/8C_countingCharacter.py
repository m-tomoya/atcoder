import sys
texts = sys.stdin.read()
texts = texts.replace(" ", "").lower()
list = "abcdefghijklmnopqrstuvwxyz"
dict = dict()
for i in range(len(list)):
    dict[list[i]] = 0

for j in range(len(texts)):
    dict[texts[j]] += 1

for k in dict.keys():
    print(k + " : " + str(dict[k]))
