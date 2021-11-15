import random
import csv
import time
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


t = int(time.time() * 1000.0)
random.seed(((t & 0xff000000) >> 24) +
            ((t & 0x00ff0000) >> 8) +
            ((t & 0x0000ff00) << 8) +
            ((t & 0x000000ff) << 24))

with open('D:\\test.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


copy_data = tuple(data)
print(copy_data)

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

            dice = (random.randint(0, len(unrolled) - 1))
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

result_list = roll(data)

for i in range(0, len(result_list)):
    result_list[i] = tuple(result_list[i])

for i in range(0, len(result_list)):
    result_list[i] = (data[i][0], result_list[i][1], result_list[i][2])

#   # backup plan
# with open('result.csv', 'w') as f:
#     write = csv.writer(f)
#     write.writerow(["email", "First Name", "Last Name"])
#     write.writerows(result_list)



# Here I will establish ssl connection and send email
port = 465  # For SSL
# this is the most unsecure way I could implement this, especially bcs its a public repo xD
# (dont worry, I will change that password later)
password = "7zzm^bT$1UcRwfeg@r9xK#Yak0e#IQzVe4a@WL%WhWef&61#2p9SHz6SqZeIDrsb"

print("To send emails enter: Y/y")
x = input()

# for debuging
res: list[str] = []
if x == "Y" or "y":

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("rybamailforcoding@gmail.com", password)

        for i in result_list:
            message = MIMEMultipart()
            message["From"] = "rybamailforcoding@gmail.com"
            message["To"] = i[0]
            message["Subject"] = "Losowanie mikołajkowe"
            body = f"Gratulacje, \ntwój los to {i[1]} {i[2]}\n\npozdro Papuez xD"
            message.attach(MIMEText(body, "plain"))
            server.sendmail("rybamailforcoding@gmail.com", i[0], message.as_string())
