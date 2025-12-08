#Notes: 
# range() prints it one in each line and list(range()) prints it all in one line
# skip by passing a third argument 
# even_numbers=list(2, 11, 2) list even numbers between 1 and 10. this list starts with 2 and adds 2  until it reaches end of list
# ** for exponents
# comprehnsion code all in one line squares = [value**2 for value in range(1,11)]

#Page 61
# 4-3 Counting to Twenty: Use a for loop to print the numbers from 1 to 20 inclusive. Three diffeent ways. 
for value in range(1,21):
    print(value)

count = list(range(1,21))
print(count)

count_twenty = [value for value in range(1,21)]
print (count_twenty)

# 4-4 Fifty: Make a list of the numbers from one to one fifity, and then use a for loop to print the numbers. 
number = [value for value in range(1,51)]
print(number)

for count in range(1,10):
    print(count)

