import time
from datetime import datetime

from playsound import playsound


def bell():
    playsound('small-bell-ring-01a.mp3')

def write(output):
    with open("TimeTracker.txt", "a") as myfile:
        myfile.write(output)
        myfile.close()

def main():
    total = 0
    imin = 20 # interval length in minutes
    now = datetime.now()
    write("Started at " + now.strftime("%H:%M:%S:%D") + '\n')
    bell()
    while(True):
        time.sleep(imin*60)
        total += 1
        now = datetime.now()
        write("Completed "+ str(total)+ " at "+ now.strftime("%H:%M:%S:%D") + '\n')
        bell()




main()