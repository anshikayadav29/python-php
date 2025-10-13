def generate_parentheses(n):
    def backtrack(s, left, right):
        # If string is complete
        if len(s) == 2 * n:
            result.append(s)
            return

        # Add '(' if we can
        if left < n:
            backtrack(s + '(', left + 1, right)
        # Add ')' if it doesn't break balance
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack("", 0, 0)
    return result

# Example usage
n = 3
print(generate_parentheses(n))
