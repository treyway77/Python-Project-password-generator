# Function to get user input for password specifications
def get_user_input():
    # Ask for password length
    while True:
        try:
            password_length = int(input("Enter the password length (between 8 and 64): "))
            if password_length < 8 or password_length > 64:
                print("Password length should be between 8 and 64.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask for character type preferences
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Return as a dictionary
    return {
        "length": password_length,
        "include_uppercase": include_uppercase,
        "include_lowercase": include_lowercase,
        "include_digits": include_digits,
        "include_special": include_special
    }

# Function to check password strength
def check_password_strength(password):
    strength = 0
    if len(password) >= 12:
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*()_+[]{}|;:,.<>?/`~" for c in password):
        strength += 1
    
    # Return strength rating (1-5)
    if strength == 5:
        return "Strong"
    elif strength == 4:
        return "Medium"
    else:
        return "Weak"

# Function to generate the password
def generate_password(length, options):
    # Define possible character sets
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*()_+[]{}|;:,.<>?/`~"
    
    # Define an empty pool of characters
    char_pool = ""

    # Add character sets to the pool based on user preferences
    if options["include_uppercase"]:
        char_pool += uppercase
    if options["include_lowercase"]:
        char_pool += lowercase
    if options["include_digits"]:
        char_pool += digits
    if options["include_special"]:
        char_pool += special

    # Ensure at least one character type is selected
    if not char_pool:
        print("Error: You must include at least one character type.")
        return None

    # Manually generate the password by picking characters from the pool
    password = ""
    for i in range(length):
        # Using an index based on the iteration number
        index = (i * 31 + len(password)) % len(char_pool)
        password += char_pool[index]

    return password

# Function to save the password to a text file with error handling
def save_password(password):
    save_option = input("Would you like to save the password to a file? (y/n): ").lower()
    if save_option == 'y':
        try:
            with open("generated_password.txt", "w") as file:
                file.write(password)
            print("Password saved to generated_password.txt.")
        except Exception as e:
            print(f"Error saving password: {e}")

# Main program flow
def main():
    print("Welcome to the Password Generator!")

    # Get user preferences
    user_input = get_user_input()

    # Generate the password
    password = generate_password(user_input["length"], user_input)
    
    if password:
        # Display the generated password
        print(f"Generated Password: {password}")
        
        # Check the strength of the password
        password_strength = check_password_strength(password)
        print(f"Password Strength: {password_strength}")
        
        # Option to save the password
        save_password(password)

if __name__ == "__main__":
    main()

       