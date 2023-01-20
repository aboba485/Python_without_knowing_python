def LOginning_in():

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
        
        code=int(code)

        print('The code came to your email!')
        code_check = input("Input your code from the Mail: ")
        code_check=int(code_check)
        while code_check!=code:
            code_check = input ("Code is not correct, input it again: ")
            code_check = int(code_check)
        