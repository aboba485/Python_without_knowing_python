import registration
import log
import sys as s
import log_out as l

registration.registr()

menu = input("""
        What is your target here?: 
1) - Log in

2) - Create a new account

3) - Log out

4) - Start!


""")

if menu == '1' or menu == 'Log in' or menu ==  'log in' or menu == 'LOG IN' or menu == 'LOG In' or menu == 'log' or menu == 'Log' or menu == 'in' or menu == 'In': 
    log.LOginning_in()
    

elif menu == '3' or menu == 'Log out' or menu ==  'log out' or menu == 'LOG OUT' or menu == 'LOG Out' or menu == 'log' or menu == 'Log' or menu == 'Out' or menu == 'out':
    l.reason()


elif menu == '2' or menu == 'Create a new account' or menu == 'create a new account' or menu == 'create a new acc' or menu == 'create a new Acc':
    registration.registr_NEW_account()

elif menu == '4' or menu == 'Start!' or menu == 'start!' or menu == 'start' or menu == 'Start' or menu == 's' or menu == 'S':
    print("")

else:
    ("Bruh you chose wrond one go and learn Python without me") 
    s.exit()