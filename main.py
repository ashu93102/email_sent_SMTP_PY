import random
import pandas
import datetime as dt
import smtplib

MY_EMAIL = "dipusharma8800@gmail.com"
MY_PASSWORD = "123456"
PLACEHOLDER = "[name]"
files = ["birthday_template/template1.txt","birthday_template/template2.txt","birthday_template/template3.txt"]

now = dt.datetime.now()
today = now.day
# print(today)
# ------------------------- CSV SECTION -------------------------- #
# orient="search" make header of file as key in dictionary"
data = pandas.read_csv("birthday_data.csv").to_dict(orient="records")
print(data)
for i in data:
    if today == i["day"]:
        try:
            with open(random.choice(files)) as file:
                letter_content = file.read()
                # Replacing [name] in template with real name of person
                birthday_letter = letter_content.replace(PLACEHOLDER, i["name"])
        except FileNotFoundError:
            print("Please Check File Path If it exists or File does not exist")
        else:
            # Below line will open mail server and close as works complete
            with smtplib.SMTP("smtp.gmail.com") as mail:
                # Below line will encrypt msg with TLS certificate
                mail.starttls()
                # For login
                # If user enter wrong login and password then it will generate an error
                # Below we try to catch that error and telling user to enter correct username as pass
                try:
                    mail.login(user=MY_EMAIL, password=MY_PASSWORD)
                except smtplib.SMTPAuthenticationError:
                    print("Please Check your user name and password.")
                else:
                    mail.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs="ashu93102@yahoo.com",
                        msg=f"Subject: Happy Birthday My Dear {i["name"]}\n\n{birthday_letter}"
                    )
