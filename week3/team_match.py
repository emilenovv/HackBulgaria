import requests
import random


def get_students():
    students = requests.get('https://hackbulgaria.com/api/students/', verify=False)
    return students


def find_courses():
    students = get_students()
    courses = []
    for course in range(len(students.json())):
        for name in range(len(students.json()[course]["courses"])):
            courses.append(students.json()[course]["courses"][name]["name"])
    courses = sorted(list(set(courses)))
    return courses


def print_list_courses():
    print("Here are the courses:")
    for index, name_of_course in enumerate(find_courses()):
        print("[" + str(index) + "] " + name_of_course)


def list_courses():
    courses_dict = {}
    for index, name_of_course in enumerate(find_courses()):
        courses_dict[index] = name_of_course
    return courses_dict


def match_teams(course_id, team_size, group_time):
    students = get_students()
    students_of_that_course = []
    dict_of_courses = list_courses()
    for course in range(len(students.json())):
        for name in range(len(students.json()[course]["courses"])):
            if students.json()[course]["courses"][name]["name"] == dict_of_courses[course_id] and students.json()[course]["courses"][name]["group"] == group_time:
                if students.json()[course]["available"] is True:
                    students_of_that_course.append(students.json()[course]["name"])
    while len(students_of_that_course) != 0:
        for i in range(team_size):
            if len(students_of_that_course) > 0:
                random_number = random.randrange(len(students_of_that_course))
                print(students_of_that_course[random_number])
                students_of_that_course.remove(students_of_that_course[random_number])
        print(15 * "=")
    return True


def team_matcher():
    print("Hello, you can use one the the following commands:")
    print("list_courses - this lists all the courses that are available now.")
    print("exit - quit the program")
    print("match_teams <course_id>, <team_size>, <group_time>")
    while True:
        choise = input("Enter command>")
        if choise == "list_courses":
            print_list_courses()
        elif choise.split()[0] == "match_teams":
            choise = choise.split()
            match_teams(int(choise[1]), int(choise[2]), int(choise[3]))
        elif choise == "exit":
            break
        else:
            print("Please enter valid command!")

if __name__ == '__main__':
    team_matcher()
