#Page 61 Try it yourself 4-6, 4-7, 4-8, 4-9

# Odd Numbers 4-6 Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
oddNumbers = list(range(1,20,1))
for value in oddNumbers:
    print(value)

# Threes 4-7 Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in the list. 
multiplesOfThree = list(range(3,31,3))
for threes in multiplesOfThree:
    print(threes)

# Cubes 4-8 Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out hte value of each cube.
cubes = []
for firstTenCubes in range(1,11):
    value = firstTenCubes ** 3
    print(value)
# Cube Comprehension 4-9 Use a list comprehension to generate a list of the first 10 cubes. 
cubeComprehension = [cubes ** 3 for cubes in range(1,11)]
print(cubeComprehension)