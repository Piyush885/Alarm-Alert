from playsound import playsound
from datetime import datetime

now = datetime.now()

alarm_time = str(input("Enter Alarm Time-----"))
current_time = str(now.strftime("%H:%M"))
#print("Current Time =", current_time)

if(current_time == alarm_time):
    while(True):
        playsound('C:/Users/LENOVO/Desktop/project/beep.mp3')
        try:
            weight = int(input())
            if weight>20:
                print("Current Timing is ",now.strftime("%H:%M"))
                print("Your Weight is",weight)
                break
        except Exception as e:
            continue
               