import imaplib, serial, struct, time
import time
from TrafficHat import TrafficHat
from EmailChecker import EmailChecker

unreadEmails = 0
email = EmailChecker()
trafficHat = TrafficHat()
newUnreadEmails = 0
trafficHat.turnOffLight()
# check for new mail every minute
try:
    while True:
        newUnreadEmails = email.sendData()
        if(newUnreadEmails > unreadEmails):
            trafficHat.turnOnLight()
            trafficHat.beep()

        unreadEmails=newUnreadEmails
        time.sleep(10)
        trafficHat.turnOffLight()
        time.sleep(50)

except (KeyboardInterrupt):
        #By doing this we reset the GPIO Pins back to default.
        print("Quitting Program")
        trafficHat.clean()


