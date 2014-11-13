import sqlite3


def get_cursor():
    conn = sqlite3.connect("company.db", isolation_level=None)
    cursor = conn.cursor()
    return cursor


def list_employees():
    cursor = get_cursor()
    result = cursor.execute("SELECT id, name, position FROM company")
    for row in result:
        print("{} - {} - {}".format(row[0], row[1], row[2]))
    return True


def get_monthly_spending_sum():
    cursor = get_cursor()
    sum = 0
    result = cursor.execute("SELECT monthly_salary FROM company")
    for row in result:
        sum += int(row[0])
    return sum


def monthly_spending():
    sum = get_monthly_spending_sum()
    print("The company is spending ${} every month.".format(sum))


def yearly_spending():
    cursor = get_cursor()
    yearly_sum = get_monthly_spending_sum() * 12
    result = cursor.execute("SELECT yearly_bonus FROM company")
    bonuses = 0
    for row in result:
        bonuses += int(row[0])
    sum = yearly_sum + bonuses
    print("The company is spending ${} every year.".format(sum))


def add_employee():
    new_name = input("Please enter the name of the new employee: ")
    new_monthly_salary = input("Please enter the monthly salary of the new employee: ")
    new_yearly_bonus = input("Please enter the yearly bonus of the new employee if no enter 0: ")
    new_position = input("Please enter at what position the new employee will be working: ")
    cursor = get_cursor()
    cursor.execute("""INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?, ?, ?, ?)"""
                   , (new_name, new_monthly_salary, new_yearly_bonus, new_position))


def delete_employee(employee_id):
    cursor = get_cursor()
    cursor.execute("DELETE FROM company WHERE id = ?", (employee_id, ))


def update_employee(employee_id):
    new_name = input("Please enter new name of the employee: ")
    new_monthly_salary = input("Please enter new monthly salary of the employee: ")
    new_yearly_bonus = input("Please enter new yearly bonus of the employee if no enter 0: ")
    new_position = input("Please enter at what new position the employee will be working: ")
    cursor = get_cursor()
    cursor.execute("UPDATE company SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ?"
                   , (new_name, new_monthly_salary, new_yearly_bonus, new_position, employee_id))


def menu():
    print("Welcome to Company Manager 1.0")
    print("There are the list of options: list_employees, add_employee, delete_employee <id>, update_employee <id>")
    while True:
        command = input("command> ")
        command = command.split()
        if command[0] == "list_employees":
            list_employees()
        elif command[0] == "add_employee":
            add_employee()
        elif command[0] == "delete_employee":
            delete_employee(command[1])
        elif command[0] == "update_employee":
            update_employee(command[1])
        elif command[0] == "quit":
            break
        else:
            print("Unknown command")

def main():
    menu()

if __name__ == '__main__':
    main()
