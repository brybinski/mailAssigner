import random
from datetime import datetime
import csv
import time


t = int( time.time() * 1000.0 )
random.seed( ((t & 0xff000000) >> 24) +
             ((t & 0x00ff0000) >>  8) +
             ((t & 0x0000ff00) <<  8) +
             ((t & 0x000000ff) << 24)   )

with open('D:\\test.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

def add_idx(lst):
    for i in range(0, len(lst)):
        lst[i].insert(0, i)

def remove_idx(lst):
    for i in lst:
        del i[0]

def roll(lst: list[list[str]]):
    count: int = len(lst)
    rolled: list[int] = []
    tmp = lst.copy()
    add_idx(tmp)
    after_roll: list[list[str]] = []

    is_correct = False

    while not is_correct:

        is_correct = True
        after_roll: list[list[str]] = []
        unrolled = tmp.copy()

        for i in range(0, count):

            if len(unrolled) == 1:
                after_roll.append(unrolled[0])
                rolled.append(i)
                break

            dice = (random.randint(0, len(unrolled)-1))
            while dice == i:
                dice = (random.randint(0, len(unrolled) - 1))

            after_roll.append(unrolled[dice])
            del unrolled[dice]
            rolled.append(dice)

        for i in range(0, len(after_roll)):
            if after_roll[i][0] == i:
                is_correct = False

    remove_idx(after_roll)
    return after_roll


test_list = [[0, "Bartosz", "Rybiński"],
             [1, "Arek", "Ryb"],
             [2, "Ania", "24Ryb"],
             [3, "Mariusz"],
             [4, "Janusz", "Rki"]]


print(roll(data))


result_list = roll(data)
for i in range(0, len(result_list)):
    result_list[i][0] = data[i][0]

with open('result.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(["email", "First Name", "Last Name"])
    write.writerows(result_list)
