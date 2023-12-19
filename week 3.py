import random
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(quantity=5, length=12):
    
    passwords = [generate_password(length) for _ in range(quantity)]
    return passwords

def main():
    print("Welcome to the Password Generator!")

    try:
        password_length = int(input("Enter the desired length of the password: "))
        password_quantity = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    passwords = generate_multiple_passwords(password_quantity, password_length)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
