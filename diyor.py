# Print your name and age using the print() function.

print("My name is Diyor, am 25 years old")

# Create variables for your name, age, and country.
name = "Diyor"
age = 25
country = "Turkey"

# Check data types of these variables using type().
print(type(name))
print(type(age))
print(type(country))

# Create two numbers and show their sum, difference, and product.
a = 5
b = 4

sum = a + b
difference = a - b
product = a * b

print(sum)
print(difference)
print(product)

# Convert a string number (like "25") into an integer and print the result.

x = "25"
y = int(x)

print(y)
print(type(x))

# Create a string and print it in uppercase and lowercase.
x = 'Diyor'
print(x.upper())
print(x.lower())

# Check if a number is positive or negative using if–else.
x = int(input("write a number: "))
if x > 0:
    print(f"{x} is positive.")
else:
    print(f"{x} is negative.")

# Check if your age is greater than 18 — print “Adult” or “Minor”.

age = int(input("How old are you? "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Use a boolean variable to show if today is a weekend (True/False).

day = input("What is day today? ")

if day in ["Saturday", "Sunday"]:
    print(f" {day} is Weekend!!!")
else:
    print(f"{day} is not weekend!!!")
