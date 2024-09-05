import json
from employee import Employee
from employee_manager import EmployeeManager
from auth import Authentication

def main():
    auth = Authentication()
    role = auth.login()

    if role == "admin":
        print("Admin panel: You can manage users.")
        while True:
            try:
                choice = input("Do you want to add a new employee? (y/n): ").lower()
                if choice not in ["y", "n"]:
                    raise ValueError("Invalid choice. Please enter 'y' for yes or 'n' for no.")
                
                if choice == "y":
                    name = input("Enter name: ")
                    surname = input("Enter surname: ")
                    position = input("Enter position: ")
                    account_number = input("Enter account number: ")
                    work_telephone = input("Enter work telephone: ")
                    Employee(name, surname, position, account_number, work_telephone)
                    print("Employee added successfully!")
                break 
            except ValueError as e:
                print(e)  

    elif role == "user":
        print("User panel: You can view employees.")
        employees = EmployeeManager.from_json('system_members.json')
        for emp in employees:
            print("---" * 10)
            emp.inf()

    else:
        print("Access denied.")

if __name__ == "__main__":
    try:
        with open('system_members.json', 'r') as file:
            pass
    except FileNotFoundError:
        with open('system_members.json', 'w') as file:
            json.dump([], file)

    main()
