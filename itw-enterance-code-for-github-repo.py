#part of into the woods
import datetime
import os
while True:
    command="wget -N http://212.71.248.238/newfile.txt"
    os.system(command)

    mode= open("newfile.txt", "r")
    choice=mode.read()
    print(choice)
    if choice=="E":
        
        print("DEBUG: ENTER MODE SELECTED")
        #entering woods
        
        pers=str(input("DEBUG: AWAITING CARD'S BARCODE"))
        print("DEBUG: searching database for barcode: "+pers)
        searchfile = open("db.csv", "r")
        for line in searchfile:
             if "searchphrase" in line: print line
             person=line
        searchfile.close()
        print("DEBUG:opening in.csv file")
        f= open("in.csv","a")
        f.write(str(datetime.datetime.now().time())+","+str(pers)+","+str(person))
        f.close()
        com="rm newfile.txt"
        #clear up for next go
        os.system(com)
   # else:
	   #os.system("rm newfile.txt")
        
        