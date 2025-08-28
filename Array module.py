import array

# Create an integer array
arr = array.array('i', [10, 20, 30, 40, 50])

# Display the array
print("Original array:", arr)

# Accessing elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# Append an element
arr.append(60)
print("After appending 60:", arr)

# Insert an element at index 2
arr.insert(2, 25)
print("After inserting 25 at index 2:", arr)

# Remove an element
arr.remove(30)
print("After removing 30:", arr)

# Pop last element
arr.pop()
print("After popping last element:", arr)

# Length of array
print("Length of array:", len(arr))

# Traversing array
print("All elements:")
for element in arr:
    print(element)
