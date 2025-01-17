import tkinter as tk
from tkinter import messagebox

# Function to get user input for password specifications
def get_user_input(length, include_uppercase, include_lowercase, include_digits, include_special):
    """Returns the options as a dictionary."""
    return {
        "length": length,
        "include_uppercase": include_uppercase,
        "include_lowercase": include_lowercase,
        "include_digits": include_digits,
        "include_special": include_special
    }

# Function to check password strength
def check_password_strength(password):
    """Evaluate the strength of the password."""
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
    
    if strength == 5:
        return "Strong"
    elif strength == 4:
        return "Medium"
    else:
        return "Weak"

# Function to generate the password
def generate_password(length, options):
    """Generate a password based on user specifications."""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*()_+[]{}|;:,.<>?/`~"
    
    char_pool = ""
    if options["include_uppercase"]:
        char_pool += uppercase
    if options["include_lowercase"]:
        char_pool += lowercase
    if options["include_digits"]:
        char_pool += digits
    if options["include_special"]:
        char_pool += special

    if not char_pool:
        print("Error: You must include at least one character type.")
        return None

    password = ""
    for i in range(length):
        index = (i * 31 + len(password)) % len(char_pool)
        password += char_pool[index]

    return password

# Function to handle password generation and display results
def generate_and_display_password(length, include_uppercase, include_lowercase, include_digits, include_special, frame):
    """Generate password and display strength, type distribution, and password."""
    options = get_user_input(length, include_uppercase, include_lowercase, include_digits, include_special)

    password = generate_password(length, options)
    
    if password:
        # Display the password and strength
        password_strength = check_password_strength(password)
        strength_label.config(text=f"Password Strength: {password_strength}")
        password_label.config(text=f"Generated Password: {password}")

        # Enable the save button
        save_button.config(state=tk.NORMAL)

# Function to save the password to a text file
def save_password(password):
    """Save password to a text file."""
    try:
        with open("generated_password.txt", "w") as file:
            file.write(password)
        messagebox.showinfo("Password Saved", "Password has been saved to generated_password.txt.")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving password: {e}")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

# Frame for password display
frame = tk.Frame(root)
frame.pack(pady=10)

# Password length input
length_label = tk.Label(root, text="Password Length (8 to 64):")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Character type selection
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.pack()
lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var)
lowercase_checkbox.pack()
digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_checkbox.pack()
special_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_checkbox.pack()

# Labels for generated password and strength
password_label = tk.Label(root, text="Generated Password: ")
password_label.pack()
strength_label = tk.Label(root, text="Password Strength: ")
strength_label.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=lambda: generate_and_display_password(
    int(length_entry.get()) if length_entry.get().isdigit() else 8,
    uppercase_var.get(),
    lowercase_var.get(),
    digits_var.get(),
    special_var.get(),
    frame
))
generate_button.pack(pady=10)

# Save Button
save_button = tk.Button(root, text="Save Password", state=tk.DISABLED, command=lambda: save_password(password_label.cget("text").replace("Generated Password: ", "")))
save_button.pack()

root.mainloop()
