import os, glob
import datetime
from os import listdir
import  time

### service name ####
WINservice = "WINservice"
Serv2016_1C = "Serv2016_1C"
#print(Serv2016_1C)

### find dir ####
os.chdir("D:\TEMP")

###### find files #######


#################### this is system date##############



dates = datetime.datetime.now().date()
####### find new file on the date #################

for file in glob.glob("*.txt"):
 #   a = os.path
    result = file.rsplit('D' ,-1 )
    tream = result[-1][0:10]
    a = os.path.getmtime(file)
    if dates==(datetime.datetime.fromtimestamp(float(a)).strftime('%Y-%m-%d')):
 #       print("work is vell")
        print (dates, "work is well", datetime.datetime.fromtimestamp(float(a)).strftime('%Y-%m-%d'))
    else:
        print("work іs not vell")
#print(date)

#### find darte from parametr file #####

#print(datetime.datetime.fromtimestamp(float(a)).strftime('%Y-%m-%d'))
#print(dates)


#print(str(a))

#files = listdir(os.chdir("D:\TEMP"))
#print(files)
for i in glob.glob("*.txt"):
    print(i)

