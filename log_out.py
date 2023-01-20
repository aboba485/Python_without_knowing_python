import sys as s
def reason():
    reason = input("""We see you want log out, why u'are u want do it?: 
    1) - I'm tired..

    2) - I don't like your app!

    3) - It is too hard fro me

    4) i worked really hard and i'm going sleep)

    5) Other reason...  
    IN YOUR ANSWER INPUT ONLY NUMBER: """)

    if reason == '1':
        print("It is normal, bro tomorrow u need work harder and harder! And don't forget about little breaks :)")
    
    elif reason == '2':
        scorrre = input("Why u dont't like it, give a reasont to us, we'll try to fix it: ")
        with open("IDLYA.txt","a") as f:
            #don't remember what does it mean ;(
            f.write(str(reason)+'\n')
        print("Thanks, bye!")
        s.exit()

    elif reason == '3':
        print("AHAHAHHA, dude how old're u?) Comunity of programmers don't need u!!!")
        s.exit

    elif reason == '4':
        reasonn = input("""
Somebody is asking me - 'Who is the best?'
My answer is this guy, YOU
Well done!!! What do u want improve in our app? """)
        with open("rtb.txt","a") as f:
            #reason for the best - rtb, abbriviation
            f.write(str(reasonn)+'\n')
        print("Thanks, bye!")
        s.exit()
    elif reason == '5':
        otr = input("Why? You can explain it here and we'll try to fix it: ")
        with open("rtb.txt","a") as f:
            #reason for the best - rtb, abbriviation
            f.write(str(reasonn)+'\n')
        print("Thank You, we'll try to fix it.")

        #otr - other reason 