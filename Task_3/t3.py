import random
import string

print("----- PASSWORD GENERATOR -----")

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Define character sets
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + numbers + symbols

# Generate password
password = ""

for i in range(length):
    random_char = random.choice(all_characters)
    password += random_char

# Display password
print("\nGenerated Password:")
print(password)
