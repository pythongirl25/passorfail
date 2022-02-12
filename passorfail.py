import time

name= input ("your name: ")
print ("hello  " + name)
time.sleep (1)
print("you will find out if you passed or failed")
time.sleep (1)
Score= input (name + " please type your score: ")
time.sleep (1)
Score = int(Score)
time.sleep (1)
if Score >= 35:
    print (name + " you passed")
else:
    print (name + " you failed")
time.sleep (1)     
print ("thank you for using this client")
