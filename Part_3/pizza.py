from time import time
from datetime import datetime

person = {}
orders = [None]
is_list_called = False
is_save_called = False


def parse_command(command):
    return tuple(command.split())


def is_valid_command(command_tuple, command):
    return command_tuple[0] == command


def is_valid_take_command(command_tuple):
    return is_valid_command and len(command_tuple) == 3 and command_tuple[0] == "take"


def is_valid_load_command(command_tuple):
    return is_valid_command and len(command_tuple) == 2 and command_tuple[0] == "load"


def list_called():
    global is_list_called
    is_list_called = True


def save_called():
    global is_save_called
    is_save_called = True


def reset_person_dict():
    global person
    person.clear()


def take_function(command):
    global is_save_called
    is_save_called = False
    if is_valid_take_command:
        name = command[1]
        price = float(command[2])
        is_save_called = False
        if name not in person:
            person[name] = price
        else:
            person[name] += price
        print("Taking order from %s for %.2f" % (name, price))
    else:
        print("Please enter name and price for the order!")


def show_status():
    if len(person) == 0:
        print("There are no current orders. \nPlease use the load command to load previous orders!")
    else:
        for name in person:
            print("%s - %.2f" % (name, person[name]))


def trigger_save():
    global is_list_called
    is_list_called = False
    global is_save_called
    is_save_called = True
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    file_name = "orders_" + stamp + '.txt'
    save_file = open(file_name, "w+")
    for name in person:
        save_file.write("%s - %.2f\n" % (name, person[name]))
    print("Saved to the current folder to " + file_name)
    save_file.close()
    orders.append(file_name)
    reset_person_dict()


def show_list():
    list_called()
    for i in range(1, len(orders)):
        print("[%d] - %s" % (i, orders[i]))


def trigger_load(command):
    if is_list_called:
        if is_save_called:
            index = int(command[1])
            print("Loading", orders[index])
            file_to_read = open(orders[index], "r")
            for line in file_to_read.readlines():
                person[line.split(" - ")[0]] = float(line.split(" - ")[1])
        else:
            print("You have not saved the current order")
            print("If you wish to discard it, type load <number> again.")
            command = parse_command(input("Enter command> "))
            if is_valid_load_command(command):
                save_called()
                trigger_load(command)
            elif is_valid_command(command, "save"):
                trigger_save()
    else:
        print("Use list command before loading!")


def unknown_command():
    unknown_command = ["Unknown command!", "Try one of the following:", "take <name> <price>", "status",
    "save", "list", "load <number>", "finish"]
    return "\n".join(unknown_command)


def main():

    while True:
        command = parse_command(input("Enter command> "))

        if is_valid_take_command(command):
            take_function(command)

        elif is_valid_command(command, "status"):
            show_status()

        elif is_valid_command(command, "save"):
            trigger_save()

        elif is_valid_command(command, "list"):
            show_list()

        elif is_valid_load_command(command):
            trigger_load(command)

        elif is_valid_command(command, "finish"):
            break

        else:
            print(unknown_command())

if __name__ == '__main__':
    main()
