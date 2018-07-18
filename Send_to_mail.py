import os, glob
import datetime

### service name, need set beckup name machines ####
listServiceBeckup = ["WINservice", "Serv2016_1C"]

### find work dir ####
workDir = "D:\TEMP"

### found character in file name #######
charFind = 'D'

###### find file extension for chack #######
extensionFile = ".txt"

##### list elements for equals emty list ####
listBack = []

#################### this is system date ##############
dates = datetime.datetime.now().date().__str__()

def chackDatafile(pathDir, *args ):
    for filename in os.listdir(pathDir):
        a = os.path.getmtime(filename)
        if filename.endswith(extensionFile) and datetime.datetime.fromtimestamp(float(a)).strftime('%Y-%m-%d')==dates and listServiceBeckup.__contains__(filename.rsplit(charFind)[0]):
            tempelementForEquals = filename.rsplit(charFind)[0]
            listBack.append(tempelementForEquals)
    balanceList = set(listServiceBeckup) - set(listBack)
    if not balanceList:
        print("have not element, -send to mail for secsesfol")
    else:
        print("hase  element send to mail is broken")

chackDatafile(os.chdir(workDir), listServiceBeckup)