# Page 65 Try It Yourself: 4-10, 4-11, 4-12

# 4-10 Slices: 
family_Names = ['Crystal', 'Rey', 'Mario', 'Elvira', 'Mayito', 'Tiburon', 'Isabel']
print(family_Names)

# Print the message The first three items in the list are: Then use a slice to print the first three itmes.
print("The first three items in the list are: ")
print(family_Names[0:3])
print(family_Names[:3])

# Print the message Three items from the middle of the list are:. Then usea slice to print the three items from the middle of the list
print("Three items from the middle of the list are: ")
print(family_Names[2:5])

# Print the message The last three items in the list are: Then use a slice to print the last three items in the list.
print("The last three items in the list are: ")
print(family_Names[4:7])
print(family_Names[4:])

# 4-11 Start with program 4-1 page 56. Make a copy of the list of pizzas, and call it friend_pizzas. Then do the following
pizza_places=['Pieology', 'Peter Pipper', 'Blaze Pizza']
friend_pizzas = pizza_places[0:3]
print(friend_pizzas)

# Add a new pizza to original and add a different pizza to the list firend_pizzas
pizza_places.append('Jets Pizza')
friend_pizzas.append('Little Cesars')

# Prove that you have two seprate lists. 
# Print the message My favorite pizzas are: and then use a for loop to print the first list. 
print("My favorite pizzas are: " ,pizza_places)

print("My favorite pizzas are: ")
for myList in pizza_places[0:4]:
    print(myList)
# Print the message My friend's favortie pizzas are: and then use a for loop to print the second list. 
print("My friend's favorite pizzas are ", friend_pizzas)
for theirList in friend_pizzas[0:4]:
    print(theirList)

#4-12 All versions of foods.py in this section have avodied using for loops when printing, to save space. 
# Choose a version of food.py and write two for loops to print each list of foods.
favorite_foods = ['wings', 'steak', 'salmon', 'pizza', 'scallops']

for foodList in favorite_foods:
    print(foodList)

for foodList2 in favorite_foods[:5]:
    print(foodList2)

