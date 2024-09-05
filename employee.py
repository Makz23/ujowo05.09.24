import uuid
import json

class Employee:
    def __init__(self, name: str, surname: str, position: str, account_number: str, work_telephone: str):
        self.unique_id = str(uuid.uuid4())
        self.name = name
        self.surname = surname
        self.position = position
        self.account_number = account_number
        self.work_telephone = work_telephone
        self.add_an_employee()

    def add_an_employee(self) -> None:
        with open('system_members.json', 'r') as file:
            members = json.load(file)
        members.append({
            'unique_id': self.unique_id,
            'name': self.name,
            'surname': self.surname,
            'position': self.position,
            'account_number': self.account_number,
            'work_telephone': self.work_telephone
        })
        with open('system_members.json', 'w') as file:
            json.dump(members, file, indent=4)

    def inf(self) -> None:
        print(f"ID: {self.unique_id}")
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Position: {self.position}")
        print(f"Account Number: {self.account_number}")
        print(f"Work Telephone: {self.work_telephone}")
