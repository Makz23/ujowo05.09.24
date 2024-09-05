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
