# 4-13 Buffet: A buffet style restaurant offers only five basic foods, store 
# them in a tuple.
basic_food = ('chicken', 'beef', 'soup', 'salad', 'pasta')

# use a for loop to print items
for basic_foods in basic_food:
    print(basic_foods)

# modify one of the items

#basic_food[0] = ('pizza') #not allowed to modify a tuple like this

# modify items 

basic_food_modify = ('chicken', 'beef', 'pizza', 'cake', 'cookies')
for basic_foods in basic_food_modify:
    print(basic_foods)