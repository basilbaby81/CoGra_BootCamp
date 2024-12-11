# ***Variable data conversion***

#****Pseudocode Block****
# Declare num1, num2, num3 and string1 with their respective values
#Convert num1 to int
#Convert num2 to float
#Convert num3 to string
#Convert string1 to int
#Print converted variable with type

#****Code Block****

#Declaring Variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

#Converting num1 to int
num1_as_int = int(num1)

#Converting num2 to float
num2_as_float = float(num2)

#Converting num3 to string
num3_as_string = str(num3)

#Converting string1 to int
string1_as_int = int(string1)

#Printing converted variable with type
print(f"num1 is {num1_as_int}, type is {type(num1_as_int)}")
print(f"num2 is {num2_as_float}, type is {type(num2_as_float)}")
print(f"num3 is {num3_as_string}, type is {type(num3_as_string)}")
print(f"string1 is {string1_as_int}, , type is {type(string1_as_int)}")
