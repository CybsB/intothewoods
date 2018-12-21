#part of into the woods
#auto updater
#This script id intended to run on boot
import os
print("auto updater for csv file which holds data for woods users (note this updater  will not update the database if there are no new people ")
com="wget -N http://212.71.248.238/db.csv"
print("updating")
os.system(com)
print("updated")