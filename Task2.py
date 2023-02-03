#Easy Task 2
num_of_inp = int(input("Enter number of inputs: "))
even = []
odd = []
output = []
for i in range(num_of_inp):   #number of iterations
    numbers= int(input("Enter numbers: "))  #vertically taken input
    if numbers%2 == 0:
         even.append(numbers)
    else:
        odd.append(numbers)
even.sort()   #sorted list of even numbers
odd.sort(reverse=True)  #reverse sorted list of odd numbers

for nums in even:
    output.append(nums)
for nums in odd:
    output.append(nums)
# print(output)  #new list of numbers

for i in output:
    print(i)       #vertical output
