  GNU nano 2.7.4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     File: ctd.py                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

#part of into the woods
import datetime
#import uniclear
import os
import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()
from time import sleep
print("clearing unicorn hat in 5 seconds")
sleep(1)
import uniclear
print("unicorn hat cleared, getting on with the rest of the code")
person=0000
#try:
 #  id, text = reader.read()
  # print(id)
   #print(text)
#finally:
 #  GPIO.cleanup()

#def rfidrd():
#       print("running rfid read function")
#       id, text = reader.read()
while True:
    command="wget -N http://212.71.248.238/newfile.txt"
    os.system("wget -N http://212.71.248.238/db.csv")
    #os.system("wget -N http://212.71.248.238/newfile.txt")
    os.system("wget -N --no-if-modified-since http://212.71.248.238/newfile.txt")
    mode= open("newfile.txt", "r")
    choice=mode.read()
    print(choice)
    if choice=="E":
        #try:
        #id, text = reader.read()
              #print(id)
              #print(text)
        #GPIO.cleanup()
        #rfidrd()
        id, text = reader.read()
        print("DEBUG: ENTER MODE SELECTED")
        #entering woods
   #     try:
                
  #         id, text=reader.read()
 #       finally:
#          GPIO.cleanup()
       
       #######################################
        #try:
          #    id, text = reader.read()
         #     print(id)
        #      print(text)
       # finally:
       #       GPIO.cleanup()







        #GPIO.cleanup()
        er=str(id)
        z1=er[0]
        z2=er[1]
        z3=er[2]
        z4=er[3]
        pers=z1+z2+z3+z4
        #pers=str(raw_input("DEBUG: AWAITING CARD'S BARCODE"))
        print("DEBUG: searching database for barcode: "+pers)
        persone=0000
        searchfilee = open("in.csv", "r")
        for line in searchfilee:
            if str(pers) in line: persone=line
        if persone!=0000:
               print("DEBUG: Rejected restarting Already in the woods")
               #import cross
               #Remove spi_bcm2835 module
               #os.system("rmmod spi_bcm2835")
               #add spi_bcm2835 module
               #os.system("modprobe spi_bcm2835")
               #os.system("python /home/pi/intw/unicorn-hat-hd/projects/unicornpaint/saves/uniclear.py")
               os.system("curl http://212.71.248.238/unib.php")
               os.system("python ctd.py")

               exit(0)
        searchfile = open("db.csv", "r")
        for line in searchfile:
             if pers in line: person=line
        #else: import cross
        if person==0000:
             #import cross
                            #Remove spi_bcm2835 module
             #os.system("rmmod spi_bcm2835")
             #add spi_bcm2835 module
             #os.system("modprobe spi_bcm2835")
             #os.system("python /home/pi/intw/unicorn-hat-hd/projects/unicornpaint/saves/uniclear.py")
             #cross here X marks the spot geddit ;)
             os.system("curl http://212.71.248.238/unib.php")
             os.system("python ctd.py")
             exit(0)
        chk1=person[0]
        chk2=person[1]
        chk3=person[2]
        chk4=person[3]
        chk=chk1 + chk2 + chk3 + chk4
        print(chk4)
        chk=chk1 + chk2 + chk3 + chk4
        if not chk==pers:
             print("GO AWAY YOU CAN'T TRICK ME")
             #rejected show the cross
             #X marks the spot
             os.system("curl http://212.71.248.238/unib.php")
             os.system("python ctd.py")
             exit(0)
             
        print(person)
        searchfile.close()
        #print(person)
        #chk1=person[0]
        #chk2=person[1]
        #chk3=person[2]
        #chk4=person[3]
        #print(chk4)
        #chk=chk1 + chk2 + chk3 + chk4
        #print("check data"+chk)
        #if not chk==pers:
              #print("GO AWAY YOU CAN'T TRICK ME")
              #rejected show the cross
              #import cross
              #exit(0)
        print("DEBUG:opening in.csv file")
        f= open("in.csv","a")
        f.write(str(datetime.datetime.now().time())+str(pers)+str(person))
        f.close()
        os.system("curl http://212.71.248.238/write.php?txt=s")
        com="rm newfile.txt"
        

        #clear up for next go
        os.system(com)
        os.system("curl http://212.71.248.238/unig.php")
        os.system("python ctd.py")
    if choice=="L":
           print("Welcome to leave mode!")
           #os.system("rm newfile.txt")
           #leave=str(raw_input("Awaiting barcode\n"))
           id ,text=reader.read()
           #GPIO.cleanup()
           er=str(id)
           z1=er[0]
           z2=er[1]
           z3=er[2]
           z4=er[3]
           leave=z1+z2+z3+z4
           
       
           print("barcode recieved")
           print("getting card's line in the csv file")
           searchfile = open("in.csv", "r")
           person=0000
           for line in searchfile:
               if str(leave) in line: person=line
           if person==0000:
                  print("DEBUG: Rejected restarting")
                  os.system("curl http://212.71.248.238/unib.php")
                  os.system("python ctd.py")
                  exit(0)
           searchfile.close()
           f = open("in.csv","r")
           lines = f.readlines()
           f.close()
           print(person)
           f=open("in.csv","w")
           for line in lines:
                 if line !=str(person):
                    f.write(line)
                    print(line+"found something to rewrite")
           os.system("curl http://212.71.248.238/writel.php?txt=s")
           f.close()
           os.system("curl http://212.71.248.238/unig.php")
           os.system("python ctd.py")

    elif choice=="A":
           id,text=reader.read()
           #GPIO.cleanup()
           os.system(str("curl http://212.71.248.238/arf.php?rfid=")+str(id))
           os.system("curl http://212.71.248.238/cl.php");
    GPIO.cleanup()




















