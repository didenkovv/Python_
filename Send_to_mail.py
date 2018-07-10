import os, glob
import datetime
import  time

date = datetime.datetime.now().date()

os.chdir("D:\TEMP")
for file in glob.glob("*.txt"):
    result = file.rsplit('_' ,-1 )
    test = result[-1][0:10]
    if date.__eq__(date):
        print("work is vell")
    else:
        print("work os not vell")
#print(date)


a  = os.path.getmtime("12.txt")
print(datetime.datetime.fromtimestamp(float(a)).strftime('%Y-%m-%d'))
print(date)


#print(str(a))
