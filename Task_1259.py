#1259
num_of_inp = int(input())
even = []
odd = []
output = []
for i in range(num_of_inp):   
    numbers= int(input())  
    if numbers%2 == 0:
         even.append(numbers)
    else:
        odd.append(numbers)
even.sort()  
odd.sort(reverse=True)  

for nums in even:
    output.append(nums)
for nums in odd:
    output.append(nums)


for i in output:
    print(i)      
