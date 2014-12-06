from expression import Expression
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from base import Base
from player import Player


def welcome_screen():
    print("Welcome to the \"Do you even math?\" game!")
    print("Here are the options:")
    print("> start")
    print("> highscores")
    print("> exit")


def enter_player_name():
    player_name = input("Enter your name> ")
    print("Welcome {}! Let the game begin!".format(player_name))
    return player_name


def check_answer(user_answer, answer):
    return user_answer == round(answer, 2)


def choose_start_highscore_or_exit():
    while True:
        command = input("command> ")
        if command == "start" or command == "highscores" or command == "exit":
            return command
        print("Incorrect command! Try again!")


def show_highscore(session):
    index = 1
    players = session.query(Player).order_by(Player.score.desc()).limit(10)
    for player in players:
        print(str(index) + ".", player)
        index += 1


def ask_questions(name, session):
    question_number = 1
    while True:
        print("Question #{}".format(question_number))
        expression = Expression.generate_expression()
        print("What is the answer to {}".format(expression))
        answer = expression.solve_expression()
        while True:
            user_answer = input("answer> ")
            if user_answer != "":
                user_answer_to_number = float(user_answer)
                break
            print("Please enter an answer!")
        if check_answer(user_answer_to_number, answer) is True:
            print("Correct")
            question_number += 1
        else:
            break
    score = (question_number - 1) * (question_number - 1)
    print("Incorrect! Ending game. You score is: {}".format(score))
    save_result(name, score, session)


def save_result(name, result, session):
    player = Player(name=name, score=result)
    session.add(player)
    session.commit()


def main():
    engine = create_engine("sqlite:///math_game.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    welcome_screen()
    while True:
        command = choose_start_highscore_or_exit()
        if command == "start":
            name = enter_player_name()
            ask_questions(name, session)
        elif command == "highscores":
            show_highscore(session)
        else:
            break


if __name__ == '__main__':
    main()