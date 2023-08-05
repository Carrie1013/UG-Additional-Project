def main(t):
    tmpL = []
    D = {}
    D = D.fromkeys(t)
    for i in range(len(t)):
        if D[t[i]] == None:
            D[t[i]] = 1
            tmpL.append(t[i])
    for i in range(0,len(tmpL)-1):
        print(tmpL[i],end=" ")
    print(tmpL[-1])

text = list()
num = int(input())
for i in range(num):
    total = int(input())
    data = input().split(' ')
    text.append([int(i) for i in data])

for i in range(len(text)):
    main(text[i])