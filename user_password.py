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
                    if len(second_password) >= 10 and any(second_password.isupper()) and any(second_password.isdigit()) and any(second_password in "!@#$%^&*()"):
                        passwords[self.username] = new_password
                        print("Password has been changed.")
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

def initials():
    return input("Name: "), input("Surname: ")

while True:
    action = input("Choose an action: [generate/modify/see/exit] ").lower()
    if action == 'generate':
        name, surname = initials()
        user = User(name, surname)
        if not user.check_existing():
            password = user.password_generator()
            print(f"Username: {user.username} Password: {password}")
    elif action == 'modify':
        name, surname = initials()
        user = User(name, surname)
        user.modify_password()
    elif action == 'see':
        admin = input("Type admin password: ")
        if admin == "admin":
            print(passwords)
    elif action == 'exit':
        break
