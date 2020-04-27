import imaplib, serial, struct, time
import Settings
from time import sleep #This imports only the sleep function from the time library.


class EmailChecker():
    def __init__(self):
        self.user= Settings.USERNAME
        self.password= Settings.PASSWORD
        self.M = imaplib.IMAP4_SSL(Settings.HOST, Settings.PORT)
        self.M.login(self.user, self.password)
        self.M.select('inbox')

    def checkMail(self):
        print("Checking emails...")
        self.M.select()
        self.unRead = self.M.search(None, 'UnSeen')
        return len(self.unRead[1][0].split())

    def sendData(self):
        self.numMessages= self.checkMail()
        #turn the string into packed binary data to send int
        return self.numMessages