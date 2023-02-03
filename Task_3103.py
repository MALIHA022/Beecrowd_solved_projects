# 3103
T = int(input())
result = []

for i in range(T):
    N = (input())
    lis = []
    zerostr = ""
    not_zero = []
    output = ""
    for nums in N:
        if nums.isdigit():
            lis.append(nums)
            lis.sort(reverse=True)

    for numbers in lis:
        if numbers != "0":
            not_zero.append((numbers))

        if numbers == "0":
            zerostr += numbers

    output += not_zero[-1]
    for zeros in zerostr:
        output += zeros
    after_zero = not_zero[:-1]
    after_zero.sort()
    for nums in after_zero:
        output += nums
    result.append(int(output))
for j in result:
    print(j)

