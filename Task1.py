# Easy Task1
n = int(input())

for i in range(n):
    inp = input().split(" ")
    inp.sort(key = len, reverse = True)
    for j in range(len(inp)):
        print(inp[j],end = " ")
    print()