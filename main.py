import time


def countdown(t):
    while t:
        hours, mins = divmod(t, 3600)
        mins, secs = divmod(t, 60)
        timer = f"{hours:02d}:{mins:02d}:{secs:02d}"
        print(timer, end="\n")
        time.sleep(1)
        t -= 1
    print("Time's up!")


timeStr = input("Insert the time to count down (h:m:s): ")
timeList = timeStr.split(":")
for i in range(len(timeList)):
    timeList[i] = int(timeList[i])

timeInSeconds = timeList[2] + timeList[1] * 60 + timeList[0] * 3600

countdown(int(timeInSeconds))
