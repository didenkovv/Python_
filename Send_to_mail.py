import os, glob
import datetime
import smtplib

### credentional for mail
mailAddressFrom = "systemmanager2019@gmail.com"
mailAddressFromPassword = "1qa@WS3ed"
mailAddressTo = "didenko.slava@gmail.com"
smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
smtpServer.starttls()
smtpServer.login(mailAddressFrom, "1qa@WS3ed")
# successMessageSubject = "This backup work is well"
successMessageText = "successful beckup"
brockenMessageText = "brocken beckup"


###

###
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
    sendMailBrockenBackup = set(listServiceBeckup) - set(listBack)
    if not sendMailBrockenBackup:
        sendMailbrocken(sendMailBrockenBackup)
        print("have not element, -send to mail for secsesfol")
    else:
        sendMailbrocken(sendMailBrockenBackup)
        print("hase  element send to mail is broken")

def sendMailbrocken(sendMailBrocken):
    send_mail_brocken = set(sendMailBrocken)
    mailBodyMassage = "\r\n".join((
        "From: %s" % mailAddressFrom,
        "To: %s" % mailAddressTo,
        "Subject: %s" % "beckup is brocken",
        "",
        "beckup is brocken" + send_mail_brocken.__str__()
    ))
    smtpServer.sendmail(mailAddressFrom, mailAddressTo, mailBodyMassage)
    smtpServer.quit()
### run for test ####
chackDatafile(os.chdir(workDir), listServiceBeckup)