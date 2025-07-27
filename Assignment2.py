# 1. Create variables
name = "Alice"
age = 25
is_student = True

# 2. Print out the type of each variable
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of is_student:", type(is_student))

# 3. Convert a string number to an integer and add 10
string_number = "45"
converted_number = int(string_number)
result = converted_number + 10
print("Result after adding 10:", result)

# 4. Convert a float to an integer and print the result
float_number = 12.87
int_number = int(float_number)
print("Float converted to integer:", int_number)

# 5. Use type() to check the type of a variable after type conversion
print("Type after converting float to int:", type(int_number))
