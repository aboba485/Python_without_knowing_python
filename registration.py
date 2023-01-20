def registr():
    name = input("Hi! Tt is a Python programming without knowing programming. Now you need input your nickname: ")

    length_name = len(name)
    


    while length_name<=2:
        name = input("Your nickname is to short, input another nick: ")
        length_name = len(name)

    mail = input("Well done! Now we'll do a quick registration. Input your mail: ")
    length_mail = len(mail)
    
    

    while mail[-10:]!='@gmail.com' and  mail[-8:] !='@mail.ru' and  mail[-10:]!='@yandex.ru':
        mail = input("Your mail is not correct, input it again: ")
        length_mail = len(mail)


    import random
    code = random.randint(100000000,100000000000)
    code = str(code)


    from email.message import EmailMessage
    import ssl
    import smtplib
 
    email_sender = 'arseny.atnashev@gmail.com'
    email_password = "VTQXZPISYJWPRNDH"
    email_receiver = mail

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

    code=int(code)

    print('The code came to your email!')
    code_check = input("Input your code from the Mail: ")
    code_check=int(code_check)
    while code_check!=code:
        code_check = input ("Code is not correct, input it again: ")
        code_check = int(code_check)
    password_user = input("Well Done! The last part of registration - you need to build your own password: ")
    legth_password = len(password_user)
    legth_password = int(legth_password) 

    
def registr_NEW_account():
    name = input("Hi! Tt is a Python programming without knowing programming. I see u need create new account, input its nickname: ")

    length_name = len(name)
    


    while length_name<=2:
        name = input("Your nickname is to short, input another nick: ")
        length_name = len(name)

    mail = input("Well done! Now we'll do a quick registration. Input your mail: ")
    length_mail = len(mail)
    
    

    while mail[-10:]!='@gmail.com' and  mail[-8:] !='@mail.ru' and  mail[-10:]!='@yandex.ru':
        mail = input("Your mail is not correct, input it again: ")
        length_mail = len(mail)


    import random
    code = random.randint(100000000,100000000000)
    code = str(code)


    from email.message import EmailMessage
    import ssl
    import smtplib
 
    email_sender = 'arseny.atnashev@gmail.com'
    email_password = "VTQXZPISYJWPRNDH"
    email_receiver = mail

    subject = 'Registration another account for <Python programming without knowing programming>'
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

    code=int(code)

    print('The code came to your email!')
    code_check = input("Input your code from the Mail: ")
    code_check=int(code_check)
    while code_check!=code:
        code_check = input ("Code is not correct, input it again: ")
        code_check = int(code_check)
    password_user = input("Well Done! The last part of registration - you need to build your own password: ")
    legth_password = len(password_user)
    legth_password = int(legth_password) 

#---------------------------------------------------------------------------------------------------------------------------------------------------