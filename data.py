class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, salary):
        employee = Employee(emp_id, name, age, salary)
        self.employees.append(employee)

    def search_by_age(self, target_age):
        result = [emp for emp in self.employees if emp.age == target_age]
        return result

    def search_by_name(self, target_name):
        result = [emp for emp in self.employees if emp.name == target_name]
        return result

    def search_by_salary(self, operator, target_salary):
        if operator == '>':
            result = [emp for emp in self.employees if emp.salary > target_salary]
        elif operator == '<':
            result = [emp for emp in self.employees if emp.salary < target_salary]
        elif operator == '<=':
            result = [emp for emp in self.employees if emp.salary <= target_salary]
        elif operator == '>=':
            result = [emp for emp in self.employees if emp.salary >= target_salary]
        else:
            result = []

        return result

    def print_results(self, results):
        for emp in results:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    employee_table = EmployeeTable()

    employee_table.add_employee("161E90", "Raman", 41, 56000)
    employee_table.add_employee("161F91", "Himadri", 38, 67500)
    employee_table.add_employee("161F99", "Jaya", 51, 82100)
    employee_table.add_employee("171E20", "Tejas", 30, 55000)
    employee_table.add_employee("171G30", "Ajay", 45, 44000)

    search_option = int(input("Choose a search parameter:\n1. Age\n2. Name\n3. Salary\n"))
    
    if search_option == 1:
        target_age = int(input("Enter the age to search for: "))
        results = employee_table.search_by_age(target_age)
    elif search_option == 2:
        target_name = input("Enter the name to search for: ")
        results = employee_table.search_by_name(target_name)
    elif search_option == 3:
        salary_operator = input("Enter the salary operator (> / < / <= / >=): ")
        target_salary = int(input("Enter the salary to compare with: "))
        results = employee_table.search_by_salary(salary_operator, target_salary)
    else:
        print("Invalid choice.")
        results = []

    if results:
        print("Search results:")
        employee_table.print_results(results)
    else:
        print("No results found.")
