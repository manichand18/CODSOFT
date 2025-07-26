import random
import string

def generate_password(length, include_uppercase, include_digits, include_symbols):
    """
    Generates a random password based on specified criteria.

    Args:
        length (int): The desired length of the password.
        include_uppercase (bool): True to include uppercase letters, False otherwise.
        include_digits (bool): True to include digits, False otherwise.
        include_symbols (bool): True to include symbols, False otherwise.

    Returns:
        str: The generated random password.
    """
    characters = string.ascii_lowercase  # Start with lowercase letters
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected for password generation.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        desired_length = int(input("Enter the desired password length: "))
        if desired_length <= 0:
            print("Password length must be a positive integer.")
        else:
            include_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            include_num = input("Include numbers? (yes/no): ").lower() == 'yes'
            include_sym = input("Include symbols? (yes/no): ").lower() == 'yes'

            try:
                generated_password = generate_password(desired_length, include_upper, include_num, include_sym)
                print(f"Generated Password: {generated_password}")
            except ValueError as e:
                print(f"Error: {e}")

    except ValueError:
        print("Invalid input for password length. Please enter a number.")