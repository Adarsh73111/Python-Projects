# Simple Main Transfer Protocol
# import smtplib
# my_email = "amisra_be23@thapar.edu"
# my_password = "avjk mojn tosy ilzi"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="yfan701@gamil.com",
#         msg="Sub:Hello\n\nThis is the body of my email"
#     )

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# print(now)
#
# date_of_birth = dt.datetime(year=2003, month=12, day=17, hour=11)
# print(date_of_birth)

import smtplib
import random
import datetime as dt

my_email = ""
my_password = ""
friend_email = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=friend_email,
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )


















