from typing import List

class Employee:
    def __init__(self, name: str):
        self.name = name
        self.pods = []

class Pod:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

class Manager:
    def assign_employee_to_pod(self, employee: Employee, pod: Pod):
        if employee is None:
            raise TypeError("Employee cannot be None")
        if pod is None:
            raise TypeError("Pod cannot be None")
        if employee in pod.employees:
            raise ValueError("Employee is already assigned to this pod")
        pod.employees.append(employee)
        employee.pods.append(pod)