import smtplib

to = input("Enter your email address\n")

content = input("Enter the email content\n")


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourPassword')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


sendemail(to, content)
