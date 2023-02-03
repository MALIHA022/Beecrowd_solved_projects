#1238
n = int(input("Enter number of test cases: "))

for i in range(n):
    string = input("Enter a String: ").split(" ")
    word1 = string[0]
    word2 = string[1]
    emptyStr = ""

    if len(word1) > len(word2):
        smaller = word2
        larger = word1
    else:
        smaller = word1
        larger = word2

    for r in range(len(smaller)):
        if r < len(smaller):
            emptyStr += word1[r]
            emptyStr += word2[r]
        else:
            emptyStr += larger[r:]

    emptyStr += larger[r + 1:]
    print(emptyStr)

