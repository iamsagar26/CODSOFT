import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters for better security.")
        return None
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(characters, length)
    
    return "".join(password)

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
