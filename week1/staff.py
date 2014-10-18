class Employee:
    def __init__ (self, name):
        self.name = name
        self.salary = 0

    def pay_salary(self):
        pass

    def get_name(self):
        return self.name

class HourlyEmployee(Employee):
    def __init__(self, name, wage):
        super().__init__(name)
        self.wage = wage

    def pay_salary(self, hours):
        diff = 0
        if hours > 40:
            diff = hours - 40
        self.salary = (hours - diff) * self.wage + diff * 1.5 * self.wage
        return self.salary

class SalariedEmployee(Employee):
    def __init__(self, name, yearly_salary):
        super().__init__(name)
        self.yearly_salary = yearly_salary

    def pay_salary(self, hours):
        self.salary = (self.yearly_salary / 1800) * hours
        return self.salary

class Manager(Employee):
    def __init__(self, name, yearly_salary, weekly_bonus):
        super().__init__(name)
        self.yearly_salary = yearly_salary
        self.weekly_bonus = weekly_bonus

    def pay_salary(self, hours):
        self.salary = (self.yearly_salary / 1800) * hours + (hours // 20) * self.weekly_bonus
        return self.salary


def main():
    staff = []
    staff.append(HourlyEmployee("Morgan, Harry", 30.0))
    staff.append(SalariedEmployee("Lin, Sally", 52000.0))
    staff.append(Manager("Smith, Mary", 104000.0, 50.0))
    for employee in staff:
        hours = int(input("Hours worked by " + employee.get_name() + ": "))
        pay = employee.pay_salary(hours)
        print("Salary: %.2f" % pay)

if __name__ == '__main__':
    main()