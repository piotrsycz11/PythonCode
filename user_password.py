#AUTHOR: Piotr Sycz
import random
import string

passwords = {}
class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.username = self.name.lower() + self.surname.lower()

    def password_generator(self):
        word = "".join(random.choice(string.ascii_letters) for _ in range(7))
        password = word + str(random.randint(1000, 9999)) + random.choice("!@#$%^&*()")
        passwords[self.username] = password
        return password

    def modify_password(self):
        if self.username not in passwords:
            print("Username does not exist.")
            return
        for i in range(4):
            actual_password = input("Type actual password: ")
            if actual_password == passwords[self.username]:
                new_password = input("Type new password: ")
                second_password = input("Type new password again: ")
                if new_password == second_password:
                    if (len(second_password) >= 6 and 
                        any(char.isupper() for char in second_password) and 
                        any(char.isdigit() for char in second_password) and 
                        any(char in "!@#$%^&*()" for char in second_password)):
                        passwords[self.username] = new_password
                        print("Password has been changed.")
                        return
                    else:
                        print("Password is not safe enough.")
                        return
                else:
                    print("Passwords are not the same.")
                    return
            else:
                self.attempts = 3 - i
                print(f"Password is not correct. You have {self.attempts} attempts left.")

    def check_existing(self):
        if self.username in passwords:
            print("Username already exists.")
            modify = input("Do you want to modify password for this user? [y/n] ")
            if modify.lower() == 'y':
                self.modify_password()
            return True
        return False
    
    def delete_user(self):
        if self.username in passwords:
            ans = input("Input admin password: ")
            if ans.lower() == 'admin':
                del passwords[self.username]
                print("User has been deleted.")
                return
        else:
            print("Username does not exist.")
            return

def initials():
    return input("Name: "), input("Surname: ")
def save_to_csv(passwords): 
    existing_users = {}
    try:
        with open("passwords.csv", "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                existing_users[key] = value
    except FileNotFoundError:
        pass
    if len(passwords) >= len(existing_users):
        existing_users.update(passwords)
        with open("passwords.csv", "w") as file:
            for key, value in existing_users.items():
                file.write(f"{key},{value}\n")
    else:
        existing_users = passwords
        with open("passwords.csv", "w") as file:
            for key, value in existing_users.items():
                file.write(f"{key},{value}\n")

while True:
    with open("passwords.csv", "r") as file:
        for _ in file:
            key, value = _.strip().split(",")
            passwords[key] = value
    action = input("Choose an action: [generate/modify/delete/see/exit] ").lower()
    if action == 'generate':
        name, surname = initials()
        user = User(name, surname)
        if not user.check_existing():
            password = user.password_generator()
            save_to_csv(passwords)
            print(f"Username: {user.username} Password: {password}")
    elif action == 'modify':
        name, surname = initials()
        user = User(name, surname)
        user.modify_password()
        save_to_csv(passwords)
    elif action == 'see':
        admin = input("Type admin password: ")
        if admin == "admin":
            with open("passwords.csv", "r") as file:
                print(file.read())
    elif action == 'delete':
        name, surname = initials()
        user = User(name, surname)
        user.delete_user()
        save_to_csv(passwords)
    elif action == 'exit':
        save_to_csv(passwords)
        break
