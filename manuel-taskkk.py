print("Emmanuel")
print("age - way too old")

##this block of code creates variables for my data and checks it's data type.
name = "Emmanuel"
age = 35
print({type(name)})
print({type(age)})

## this block of code creates two numbers and show their sum, diff & product
p = 16
r = 5
print(f"  p = {p}")
print(f"  r = {r}")
sum = p + r
diff = p - r
product = p * r
print(f"the sum, difference and product of p and r are {sum}, {diff}, {product}")
print()

##this block of code converts a string to integer
x = "10"
print(f" the integer format of \"10\" is {(int(x))}")

##this block of code creates and prints a string in different cases.
y = "Engineering"
print(y)
print(f" \"Engineering\" in upper case is {(y).upper()}")
print(f" \"Engineering\" in lower case is {(y).lower()}")
print(f" \"Engineering\" in title case is {(y).title()}")
print()

##this block of code checks if a number is positive or negative
number = int(input("Enter a number: "))
if number == "":
    print("You didn't enter a number.")
elif number < 0:
    print("You entered a negative number.")
else:
    print("You entered a positive number.")
print()

## this line of code checks if the user is an adult or minor
your_age = int(input("pls enter your age: "))
if your_age == "":
    print("You didn't enter your age.")
elif your_age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
print()

## this line of code checks if it's the weekend
day = input("Enter a day: ").lower()
if day == "":
    print("You didn't enter a day.")
elif day == "friday" or day == "saturday" or day == "sunday":
    print("it's the weekend.")
else:
    print("it's the weekend.")
print()

