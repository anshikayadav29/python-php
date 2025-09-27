import random
import string

def generate_password(length=12):
    # Characters: letters + digits + punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Random choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example run
print("Generated Password:", generate_password(16))
