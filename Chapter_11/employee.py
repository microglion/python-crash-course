class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        
    def give_raise(self, raise_amount = 5000):
        self.salary += raise_amount
        return self.salary

if __name__ == '__main__':
    new_employee = Employee('John', 'Wick', 80000)
    new_employee.give_raise()
    print(f"New salary after raise is: £{new_employee.salary}")
    new_employee.give_raise(5000)
    print(f"New salary after 2nd raise: £{new_employee.salary}")
