import json

class Authentication:
    def __init__(self):
        self.users = {
            "admin": {"password": "admin123", "role": "admin"},
            "user1": {"password": "user123", "role": "user"},
            "user2": {"password": "user456", "role": "user"}
        }

    def login(self):
        while True:
            try:
                username = input("Enter username: ")
                password = input("Enter password: ")

                if username in self.users and self.users[username]["password"] == password:
                    print(f"Welcome, {username}!")
                    return self.users[username]["role"]
                else:
                    raise ValueError("Invalid credentials, try again.")
            except ValueError as e:
                print(e)

    def save_users(self):
        with open('users.json', 'w') as file:
            json.dump(self.users, file, indent=4)

    def edit_user_role(self):
        username = input("Enter the username to modify: ")
        if username in self.users:
            new_role = input(f"Enter new role for {username} (current role: {self.users[username]['role']}): ")
            self.users[username]["role"] = new_role
            self.save_users()
            print(f"User {username}'s role updated to {new_role}.")
        else:
            print("User not found.")