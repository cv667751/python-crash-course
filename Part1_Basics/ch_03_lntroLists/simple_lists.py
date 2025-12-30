# 3-1 Names Page 36 Store the names of a few friends in a list called names. 
# Print each person's namee by accessing each element, one by one. 
friends_names = ["Rey", "Elvira", "Mario", "Mario_Jr"]
print(friends_names[0])
print(friends_names[1])
print(friends_names[2])
print(friends_names[3])
print(friends_names)

# 3-2 Greetings Print a message to each of the friends from 3-1, 
# the message should be the same to each person just change the name
message = "Hi, I miss you "
print(message + friends_names[0])

message = f"Hi, I miss you  {friends_names[1]}"
print(message)

message = "Hi, I miss you "
print(message + friends_names[2])

message = f"Hi, I miss you  {friends_names[3]}"
print(message)

# 3-3 Your Own List Make a list of vehicles. 
# Use list to print a series of statements about the vehicles. 
transportation = ['honda', 'ford', 'bmw', 'porshe']
statement = f"I want to own a {transportation[0]}"
print(statement)
statement = f"I want to own a {transportation[1]}"
print(statement)
statement = f"I want to own a {transportation[2]}"
print(statement)
statement = f"I want to own a {transportation[3]}"
print(statement)

#3-9 Dinner Guests: Working with one of the programs from Exercies 3-4 to 3-7 
# use len() to print a message indicating the number of people.
print(len(transportation))
print(len(friends_names))
