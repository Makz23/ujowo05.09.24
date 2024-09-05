import json
from typing import List, Dict
from employee import Employee

class EmployeeManager:
    @staticmethod
    def from_dict(data: Dict[str, str]) -> Employee:
        return Employee(
            name=data['name'],
            surname=data['surname'],
            position=data['position'],
            account_number=data['account_number'],
            work_telephone=data['work_telephone']
        )

    @staticmethod
    def from_json(file_path: str) -> List[Employee]:
        with open(file_path, 'r') as file:
            data = json.load(file)
            employees: List[Employee] = []
            for item in data:
                employee = EmployeeManager.from_dict(item)
                employees.append(employee)
        return employees
    
    @staticmethod
    def save_employees(file_path: str, employees: List[Dict]):
        with open(file_path, 'w') as file:
            json.dump(employees, file, indent=4)

    @staticmethod
    def edit_employee(file_path: str, employee_id: str):
        with open(file_path, 'r') as file:
            employees = json.load(file)
        
        for emp in employees:
            if emp['unique_id'] == employee_id:
                print(f"Editing employee: {emp['name']} {emp['surname']}")
                emp['name'] = input(f"Enter new name (current: {emp['name']}): ") or emp['name']
                emp['surname'] = input(f"Enter new surname (current: {emp['surname']}): ") or emp['surname']
                emp['position'] = input(f"Enter new position (current: {emp['position']}): ") or emp['position']
                emp['account_number'] = input(f"Enter new account number (current: {emp['account_number']}): ") or emp['account_number']
                emp['work_telephone'] = input(f"Enter new work telephone (current: {emp['work_telephone']}): ") or emp['work_telephone']
                break
        else:
            print("Employee not found.")
            return

        EmployeeManager.save_employees(file_path, employees)
        print("Employee updated successfully.")