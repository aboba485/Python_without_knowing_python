
import sys as s
menu = input("""
           What is your target here?: 
1) - Log in

2) - Create an account

3) - Log out

""")

if menu == '1' or menu == 'Log in' or menu ==  'log in' or menu == 'LOG IN' or menu == 'LOG In' or menu == 'log' or menu == 'Log' or menu == 'in' or menu == 'In': 
    print("")


elif menu == '3' or menu == 'Log out' or menu ==  'log out' or menu == 'LOG OUT' or menu == 'LOG Out' or menu == 'log' or menu == 'Log' or menu == 'Out' or menu == 'out':
    print("ojuh")

else:
    ("Bruh you chose wrond one go and learn Python without me") 
    s.exit()


def log_in():
    mail2 = input("Hi if u already have an account imput here your Email")
    print("Yep! We have your acc in our data base!, Now on your email will arrive an email!")
    print("Sending...")
    length_mail2 = len(mail2)
    
    

    while mail2[-10:]!='@gmail.com' and  mail2[-8:] !='@mail.ru' and  mail2[-10:]!='@yandex.ru':
        mail2 = input("Your mail is not correct, input it again: ")
        length_mail2 = len(mail2)

    print("Yep! We have your acc in our data base!, Now on your email will arrive an email!")
    print("Sending...")
   

    import random
    code = random.randint(100000000,100000000000)
    code = str(code)

    from email.message import EmailMessage
    import ssl
    import smtplib

    email_sender = 'arseny.atnashev@gmail.com'
    email_password = "VTQXZPISYJWPRNDH"
    email_receiver = mail2

    subject = 'Registration for <Python programming without knowing programming>'
    body = """
    Nobody should knows this secret code
    ---------------------------------
    code: 
    """
    body = body+code

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    