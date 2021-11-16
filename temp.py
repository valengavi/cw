# Step 1
from random import randint
numbers = []
odd = []
even = []
for i in range(100):
    numbers.append(randint(1, 100))

print(numbers)
print("")

# Step 2
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
print("The number of odd numbers in the list is " + str(len(odd)) + ", the smallest is " + str(min(odd)) + " and the largest is "+ str(max(odd)))
print("")

# Step 3
print("The number of even numbers in the list is " + str(len(even)) + ", the smallest is " + str(min(even)) + " and the largest is "+ str(max(even)))
print("")
# Step 4
mult5 = []
for i in numbers:
    if i % 5 == 0:
        mult5.append(i)

print("The number of multiples of five in the list is " + str(len(mult5))+ ", the smallest is " + str(min(mult5)) + " and the largest is "+ str(max(mult5)))
print("")
# Step 5
mult10 = []
for i in numbers:
    if i % 10 == 0:
        mult10.append(i)
print("The number of multiples of five in the list is " + str(len(mult10))+ ", the smallest is " + str(min(mult10)) + " and the largest is "+ str(max(mult10)))
print("")

# Step 6
print(sorted(numbers))