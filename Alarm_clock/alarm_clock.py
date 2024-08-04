from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # 02d gives in 2 decimal place
        print(
            f"{CLEAR_AND_RETURN} Alarm will sound in {minutes_left:02d} : {seconds_left:02d}")
    playsound("Alarm_clock/Alarm.mp3")


minutes = int(input("Enter number of minutes to run: "))
seconds = int(input("Enter number of seconds to run: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)
