from faker import Faker
from os import path, system, name
from time import sleep
import datetime

fake = Faker()

HIGH_SCORES_FOLDER = "data/high_scores/"

DEMO_USER = "DEMO"

# prints a date in a pretty format
def print_date(date): 
    print(date)


def valid_answer(answer, date ):
    correct_week_day_short = date.strftime("%a").upper()
    correct_week_day_long = date.strftime("%A").upper()

    answer = answer.upper()
    correct = False

    if answer == correct_week_day_short or answer == correct_week_day_long:
        clear_screen()
        print("correct")
        correct = True
        sleep(0.5)
        clear_screen()
    else:
        print("Wrong")
        print("Correct solution: " + correct_week_day_short)
        

    return correct
    

def exit_game():
    clear_screen()
    print("Goodbye!")
    sleep(0.5)
    clear_screen()
    quit()

def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def game_over():
    print("Try again?")
    answer = input("(y)yes OR (n)no: ").upper() 
    if answer != 'Y':
        exit_game()

    # otherwise game is reset and screen needs to be cleared 
    clear_screen()

def set_high_score(score, user):
    save = HIGH_SCORES_FOLDER + user + ".score"
    current_high_score = read_high_score(user)

    if int(current_high_score) < score:
        f = open(save, "w")
        f.write(str(score))
        f.close()

def read_high_score(user):
    save = HIGH_SCORES_FOLDER +user + ".score" 
    if path.isfile(save):
        f = open(save, "r")
        current_score = f.readline()
        f.close()
        return current_score
    return 0

def get_user():
    return input("Type in user name: ")

def welcome_prompt():
    print("Welcome to week day guesser")
    print("Try and guess the week day with given dates")
    return 

# actual game 
def main():
    clear_screen()
    welcome_prompt()
    user = get_user()
    high_score = read_high_score(user)
    score = 0
    finished = False
    clear_screen()
    while not finished:
        start_year = 1900
        end_year = 2100
        random_date = fake.date_between_dates(datetime.date(start_year, 1,1) , 
                                              datetime.date(end_year,12,31))
        print("High score: " + str(high_score))
        print("Current score: " + str(score))
        print_date(random_date)
        answer = input().upper()

        if answer == "Q":
            set_high_score(score , user)
            exit_game()

        if not valid_answer(answer, random_date):
            set_high_score(score, user)
            game_over()
            
            # resets game
            high_score = read_high_score(user)
            score = -1  
        # finished = not valid_answer(answer, random_date) 
        score+=1
    
main()
