class Employee:
    def __init__(self):
        self.name = ''
        self.position = ''
        self.salary = 0

employee = Employee()

employee.name = 'John Doe'
employee.position = 'Manager'
employee.salary = 5000

print(f"Имя: {employee.name}")
print(f"Должность: {employee.position}")
print(f"Зарплата: {employee.salary}")