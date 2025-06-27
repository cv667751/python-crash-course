# 2-7 Page 25
# Use a variable to represent a person's name, and include some whitespace characters 
# at the beginning and end of the name. Use \t and \n at least once 
# print the name once, so the white space is displayed 
# then print the name using each of the three stripping functions, lstrip(), rstrip(), strip()

name = "    \tcrystal\n   "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())