# Create the dictionary
my_dict = {}
 
# Now using for statement for it
for i in range(97, 97 + 26):
    # Map character to ascii value
    my_dict[chr(i)] = i
 
# Print the dictionary
print(my_dict)