#3-10 Ever Function Page 45
# Make a list
colors = ['red', 'blue', 'yellow', 'orange', 'pink', 'white']

# Print firt item and last item
print(colors[0])
print(colors[-1])

# Modify Items change orange to brown
colors[3] = 'brown'
print(colors)

# Add Items at end of list using append
colors.append('oragne')
print(colors)

# Insert items anywere on the list using index position
colors.insert(3,'green')
print (colors)

# Remove item from list using the del
del colors[3]
print(colors)
#or just use remove by value
# colors.remove('white)

# Use pop() to remove (removes the last item (top of the stack) and but can still access)
print('Space Space Space')
popped_colors = colors.pop()
print(colors)
print(popped_colors)
# Can use pop for any item on list using index position
# first = colors.pop(0)

print('Space Space Space')
# Use sort() permanently sort a list 
colors.sort()
print(colors)

# sort(Reverse=True) reverse-alpha permanently
colors.sort(reverse=True)
print(colors)

# Use sorted() temprarily sort a list
print(sorted(colors))

# .reverse() to reverse to original order
colors.reverse()
print(colors)

# Find the length of a list
print(len(colors))