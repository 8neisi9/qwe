class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.position = ''
        self.salary = salary

employee = Employee('John Doe', 5000)

print(f"Имя: {employee.name}")
print(f"Должность: {employee.position}")
print(f"Зарплата: {employee.salary}")