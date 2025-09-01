# 1. Print a simple message
print("Hello, World!")

# 2. Print multiple values
name = "Anshika"
age = 20
print("Name:", name, "Age:", age)

# 3. Print using f-strings (modern way)
print(f"My name is {name} and I am {age} years old.")

# 4. Print with separator and end
print("Apple", "Banana", "Mango", sep=", ")
print("Hello", end=" ")
print("World")

# 5. Print multiline text
print("""This is
a multi-line
text in Python.""")

# 6. Print using format()
print("My name is {} and I am {} years old.".format(name, age))

# 7. Print special characters
print("He said: \"Python is awesome!\"")
print("Line1\nLine2\tTabbed")

# 8. Print a list
fruits = ["Apple", "Banana", "Mango"]
print("Fruits list:", fruits)

# 9. Print a dictionary
student = {"name": "Anshika", "age": 20, "course": "Python"}
print("Student details:", student)

# 10. Print numbers in a loop
for i in range(1, 6):
    print(i, end=" ")
print()  # for new line

# 11. Print a pattern (stars)
for i in range(1, 6):
    print("*" * i)

# 12. Print formatted table
for i in range(1, 6):
    print(f"{i} x {i} = {i*i}")
