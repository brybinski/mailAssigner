import smtplib
import ssl


port = 465  # For SSL
password = "7zzm^bT$1UcRwfeg@r9xK#Yak0e#IQzVe4a@WL%WhWef&61#2p9SHz6SqZeIDrsb"


lst = []



message = f"""\
Subject: Hi there

This message is sent from Python."""

# # Create a secure SSL context
# context = ssl.create_default_context()
#
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("rybamailforcoding@gmail.com", password)
#
#
#     server.sendmail("rybamailforcoding@gmail.com", "158060@student.uwm.edu.pl", message)
