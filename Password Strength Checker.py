# Password Strength Checker

# Ask the user to enter a password
password = input("Enter your password: ")

# Variables to store password features
has_upper = False
has_number = False
has_symbol = False

# List of allowed symbols
symbols = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/~`"

# Check each character in the password
for char in password:

    if char.isupper():          # Check for uppercase letters
        has_upper = True

    elif char.isdigit():        # Check for numbers
        has_number = True

    elif char in symbols:       # Check for special symbols
        has_symbol = True

# Calculate password score
score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Add points for each security feature
if has_upper:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1

# Display the result
print("\nPassword Analysis")
print("----------------------")
print("Password Length :", len(password))
print("Contains Uppercase :", has_upper)
print("Contains Number :", has_number)
print("Contains Symbol :", has_symbol)

# Decide password strength
if score <= 1:
    print("Password Strength: Weak")

elif score <= 3:
    print("Password Strength: Medium")

else:
    print("Password Strength: Strong")