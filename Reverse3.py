def reverse_string(s):
    if len(s) == 0:  # Base case
        return s
    else:
        return reverse_string(s[1:]) + s[0]  # Recursive step

# Test
text = "hello"
print(f"Reversed string: {reverse_string(text)}")
