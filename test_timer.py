import time
import threading
from os import system


def timer(max_time): 
    running_time = 0
    while running_time < max_time:
        print(running_time)
        running_time+=1
        time.sleep(1)
    print("Time's up!")
    quit()

def get_user_input():
    something = input("something: ")
    print(something)

    return something


if __name__ == "__main__":
    timer_thread = threading.Thread(target=timer, args=[10])
    user_input_thread = threading.Thread(target=get_user_input)
    timer_thread.start()
    user_input_thread.start()

    timer_thread.join()
    user_input_thread.join()




