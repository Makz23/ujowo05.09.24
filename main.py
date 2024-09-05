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
                print("\nOptions: ")
                print("1. Add a new employee")
                print("2. Edit an existing employee")
                print("3. Edit user roles")
                print("4. Exit")

                choice = input("Choose an option: ").strip()

                if choice == "1":
                    name = input("Enter name: ")
                    surname = input("Enter surname: ")
                    position = input("Enter position: ")
                    account_number = input("Enter account number: ")
                    work_telephone = input("Enter work telephone: ")
                    Employee(name, surname, position, account_number, work_telephone)
                    print("Employee added successfully!")

                elif choice == "2":
                    employees = EmployeeManager.from_json('system_members.json')
                    print("Employees:")
                    for emp in employees:
                        print(f"{emp.unique_id}: {emp.name} {emp.surname}")
                    emp_id = input("Enter the ID of the employee to edit: ")
                    EmployeeManager.edit_employee('system_members.json', emp_id)

                elif choice == "3":
                    auth.edit_user_role()

                elif choice == "4":
                    print("Exiting admin panel.")
                    break

                else:
                    raise ValueError("Invalid option. Please select a valid number.")
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