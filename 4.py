class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def get_name(self):
        return self.name
        
    def get_salary(self):
        return self.salary
        
    def increase_salary(self):
        self.salary = self.salary * 1.1

emp = Employee('John', 5000)
print(emp.get_name())  # Output: John
print(emp.get_salary())  # Output: 5000

emp.increase_salary()
print(emp.get_salary())  # Output: 5500


