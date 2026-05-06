import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password (leave blank to generate): ")

    if password == "":
        password = generate_password()
        print(f"Generated Password: {password}")

    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {username} | {password}\n")

    print("Password saved successfully.\n")

def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            data = file.readlines()
            if not data:
                print("No passwords saved yet.\n")
            else:
                print("\nSaved Passwords:")
                for line in data:
                    print(line.strip())
    except FileNotFoundError:
        print("No password file found.\n")

def search_password():
    search = input("Enter website to search: ")

    try:
        with open("passwords.txt", "r") as file:
            found = False
            for line in file:
                if search.lower() in line.lower():
                    print(line.strip())
                    found = True
            if not found:
                print("No match found.\n")
    except FileNotFoundError:
        print("No password file found.\n")

def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Generate Password")
        print("2. Save Password")
        print("3. View Passwords")
        print("4. Search Password")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Generated Password:", generate_password())
        elif choice == "2":
            save_password()
        elif choice == "3":
            view_passwords()
        elif choice == "4":
            search_password()
        elif choice == "5":
            print("Goodbye ")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()