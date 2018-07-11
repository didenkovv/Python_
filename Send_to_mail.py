import os, glob
import datetime
import  time

###### find files #######


#################### this is system date##############
WINservice = "WINservice"
Serv2016_1C = "Serv2016_1C"
print(Serv2016_1C)


dates = datetime.datetime.now().date()
####### find new file on the date #################
os.chdir("D:\TEMP")
for file in glob.glob("*.txt"):
    result = file.rsplit('_' ,-1 )
    test = result[-1][0:10]
    if dates.__eq__(test):
        print("work is vell")
    else:
        print("work os not vell")
#print(date)

#### find darte from parametr file #####
a = os.path.getmtime("12.txt")
print(datetime.datetime.fromtimestamp(float(a)).strftime('%Y-%m-%d'))
print(dates)


#print(str(a))
