import json

class Authentication:
    def __init__(self):
        self.users = {
            "admin": {"password": "admin123", "role": "admin"},
            "user1": {"password": "user123", "role": "user"},
            "user2": {"password": "user456", "role": "user"}
        }

    def login(self):
        while True:  # Pętla, która wymaga poprawnych danych logowania
            try:
                username = input("Enter username: ")
                password = input("Enter password: ")

                if username in self.users and self.users[username]["password"] == password:
                    print(f"Welcome, {username}!")
                    return self.users[username]["role"]
                else:
                    raise ValueError("Invalid credentials, try again.")
            except ValueError as e:
                print(e)  # Wyświetla wiadomość o błędzie i ponawia logowanie

    def save_users(self):
        with open('users.json', 'w') as file:
            json.dump(self.users, file, indent=4)
