class Employee:
    def __init__ (self, name, wage):
        self.name = name
        self.wage = wage
        self.salary = 0

    def pay_salary():
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, wage):
        super().__init__(name, wage)

    def pay_salary(self, hours):
        diff = 0
        if hours > 40:
            diff = hours - 40
        self.salary = (hours - diff) * self.wage + diff * 1.5 * self.wage
 

galin = HourlyEmployee("Galin", 30.0)
galin.pay_salary(45)
print(galin.salary)