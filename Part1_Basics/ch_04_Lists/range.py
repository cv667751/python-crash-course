#Notes: 
# range() prints it one in each line and list(range()) prints it all in one line
# skip by passing a third argument 
# even_numbers=list(range(2, 11, 2)) list even numbers between 1 and 10. this list starts with 2 and adds 2  until it reaches end of list
# ** for exponents
# comprehnsion code all in one line squares = [value**2 for value in range(1,11)]

#Page 61
# 4-3 Counting to Twenty: Use a for loop to print the numbers from 1 to 20 inclusive. Three diffeent ways. 
#Method 1
for value in range (1, 21):
    print(value)

#Method 2
numbers = list(range(1,21))
print(numbers)

#Method 3
count = []
for values in range(0,20):
    sum = values + 1
    count.append(sum)
print(count)

#List comprehensions Method 4
counting = [num + 1 for num in range(0,20)]
print(counting)

# 4-4 One Million but changed to Fifty: Make a list of the numbers from one to one fifty, and then use a for loop to print the numbers. 
#Method 1
for value in range(1,51):
    print(value)

#Method 2
numbers = list(range(1,51))
print(numbers)

#Method 3
count = []
for values in range(1,51):
    count.append(values)
for num in count:
    print(num)

#Method 4
counting = [num for num in range(1,51)]
print(counting)