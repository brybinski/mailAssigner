from smtplib import SMTP
import ssl

port = 465  # For SSL
password = "7zzm^bT$1UcRwfeg@r9xK#Yak0e#IQzVe4a@WL%WhWef&61#2p9SHz6SqZeIDrsb"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("rybamailforcoding@gmail.com", password)
    # TODO: Send email here
