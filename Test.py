from datetime import datetime
from time import sleep
from random import randint
from time import time
i = 10
odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

#sleeps = sleep(5)

for i in range(5):
 #   s = randint(1, 89)
 #   print(s)
    right_this_minute = datetime.today().minute
    sleep(10)
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
        wait_time = randint(1, 60)
        time.sleep(wait_time)
