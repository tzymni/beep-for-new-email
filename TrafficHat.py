import RPi.GPIO as IO  #This line imports RPi.GPIO but sets it to IO meaning we can type in IO on every line instead of RPi.GPIO.
from time import sleep #This imports only the sleep function from the time library.

IO.setmode(IO.BCM)
class TrafficHat():
    def __init__(self):
        self.YELLOW = 23
        self.BUZZER = 5
        self.outputs = [self.YELLOW, self.BUZZER]

        for output in self.outputs:
            #This will then pass the number of the output to the variable output
            IO.setup(output,IO.OUT)

    def turnOnLight(self):
        IO.output(self.YELLOW, 1)

    def turnOffLight(self):
        IO.output(self.YELLOW, 0)

    def beep(self):
        IO.output(self.BUZZER, 1)
        sleep(1)
        IO.output(self.BUZZER, 0)

    def clean(self):
        IO.cleanup()