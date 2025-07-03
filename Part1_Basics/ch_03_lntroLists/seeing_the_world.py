# 3-8 Seing the world: Think of at least places int he world you'd like to visit. 
# Store the locations in a list, not in alpha order
vacation = ["Hawaii", "Washington", "Colorado", "California"]

# print list in original order (raw python list)
print(vacation)

# use sorted() to print your list in alpha order without modifying the actual list
print(sorted(vacation))

# show that your list is still in its original order by printing it 
print(vacation)

# use sorted() to print list in reverse-alpha without chaning the original list
print(sorted(vacation, reverse=True))

# show that list is still in original order
print(vacation)

# use reverse() to change the order of your list and print the list to show order has changed
vacation.reverse()
print(vacation)

# use reverse() to change the order again, print the list to show it's back to original order
vacation.reverse()
print(vacation)

# use sort() to change your list so it's stored in alpha order and print the list to show order has been changed
vacation.sort()
print(vacation)

# use sort() to change your list so it's stored in reverse-alpha order print the list to show that its order has changed. 
vacation.sort(reverse=True)
print(vacation)