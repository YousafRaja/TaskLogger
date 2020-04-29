import time
from datetime import datetime

from playsound import playsound


def bell():
    playsound('small-bell-ring-01a.mp3')

def main():
    total = 0
    imin = 20 # interval length in minutes
    print("Starting Logger")
    bell()
    while(True):
        time.sleep(imin*60)
        total += 1
        now = datetime.now()
        output = "Completed "+ str(total)+ " at "+ now.strftime("%H:%M:%S") + '\n'
        with open("TimeTracker.txt", "a") as myfile:
            myfile.write(output)
            myfile.close()
        bell()




main()