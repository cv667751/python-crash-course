# 3-4 Guest List Make a list that includes at least 3 people and use your list to print a message inviting them to dinner.
guestList = ['Husband', 'Mom', 'Dad', 'Brother']
invite = f"You are invited to the dinner next weekend, hope you can make it"
print(f"{invite} {guestList[0]}")
print(f"{invite} {guestList[1]}")
print(f"{invite} {guestList[2]}")
print(f"{invite} {guestList[3]}")

# 3-5 Changing Guest List One of the guests can't make it.
# Add a print call at end with the person who can't make it. 
print(f"Sorry you can't make it, {guestList[3]}.")
# Modify list, replace the name of the guest who can't make it with a new person. 
guestList[3] = "Aunt"
# Print a second set of invites of guest list. 
print(f"{invite} {guestList[0]}")
print(f"{invite} {guestList[1]}")
print(f"{invite} {guestList[2]}")
print(f"{invite} {guestList[3]}")

# 3-6 More Guests Invite three more guests. 
# Add a print call to inform about a bigger table was found
print("Hello guests, we have found a bigger table for dinner! ")
# Use insert() to add a guest at beggining of list
guestList.insert(0, 'Isabel')

# Use insert() to add a guest middle of list
guestList.insert(2, 'Tiburon')

# Use append() to add a ne guest at end of list
guestList.append('Hazzard')

# Print new invites 
print(f"{invite} {guestList[0]}")
print(f"{invite} {guestList[1]}")
print(f"{invite} {guestList[2]}")
print(f"{invite} {guestList[3]}")
print(f"{invite} {guestList[4]}")
print(f"{invite} {guestList[5]}")
print(f"{invite} {guestList[6]}")

# 3-7 Shrinking Guest List Bigger table is not arriving on time and have space only for two guests. 
# Let guests know only two can be invited because table is going to arrive another day. 
print("Hello everyone, sorry but we have change of plans. The bigger table will not make it on time for the dinner. Only two of you will be able to attend. ")

# Use pop to remove guests one at a time, until only two remain. Each time you pop a name, print a message for them. 
popped_guestList = guestList.pop()
print(f"Sorry we had to remove you from guest list {popped_guestList}")
popped_guestList = guestList.pop()
print(f"Sorry we had to remove you from guest list {popped_guestList}")
popped_guestList = guestList.pop()
print(f"Sorry we had to remove you from guest list {popped_guestList}")
popped_guestList = guestList.pop()
print(f"Sorry we had to remove you from guest list {popped_guestList}")
popped_guestList = guestList.pop()
print(f"Sorry we had to remove you from guest list {popped_guestList}")
# Print a message to the two guests who are still coming.
print(f"Hey you are still in the list for dinner! {guestList[0]}")
print(f"Hey you are still in the list for dinner! {guestList[1]}")
# Use del to remove the last two names of the list, print the list to make sure it is empty. 
del guestList[0]
print(guestList)
del guestList[0]
print(guestList)