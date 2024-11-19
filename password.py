
import string
import random

def generate_password(length, complexity):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Different complexity levels
    if complexity == 1:  # Only lowercase
        char_pool = lower
    elif complexity == 2:  # Lowercase + uppercase
        char_pool = lower + upper
    elif complexity == 3:  # Lowercase + uppercase + digits
        char_pool = lower + upper + digits
    elif complexity == 4:  # Lowercase + uppercase + digits + symbols
        char_pool = lower + upper + digits + symbols

    else:
        print("Invalid complexity level. Choose between 1 and 4.")
        return None
    
    # Generate password from the character pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Input from user
length = int(input("     Enter the  length of the password as you want : "))
print ("these are the complexity levels we are having choose what you want")
print("   1)Simple\n    2)Medium\n    3) Strong\n    4) Very Strong) ")
complexity = int(input("Enter the complexity level :")) 

# Generate and display the password
generated_password = generate_password(length, complexity)

if generated_password:
    print(f"Generated Password: {generated_password}")