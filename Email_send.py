# libraries import
import smtplib

# send mail put
lists =['parikhdhruv05@gmail.com']

# connection in port no:-all Email same number in 587
connection = smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo()
connection.starttls()

# connection in first your email id and send email password
connection.login('parikhdhruv05@gmail.com','pniqhkgxgoqylvhi')
# parikhdhruv05@gmail.com:= your Email put
# pniqhkgxgoqylvhi := This password is Email password not.
# step-1: open google account
# step-2: Security selected
# step-3: 2-Step Verification selected and completed step
# step-4: search 'app password'
# step-5: Select the app and device for which you want to generate the app password.
# step-6: select app ('other') input('python')
# step-7: Enter  Generate

for i in lists:
    connection.sendmail('parikhdhruv05@gmail.com', i ,'Subject:python \n\n Hello my name is Dhruv Parikh')

    print(f"mail send Done {i}")
connection.quit()

