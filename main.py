import time


def countdown(t):
    while t:
        hours, mins = divmod(t, 3600)
        onlyMinutesAndSeconds = t - hours * 3600
        mins, secs = divmod(onlyMinutesAndSeconds, 60)
        timer = f"{hours:02d}:{mins:02d}:{secs:02d}"
        print(timer, end="\n")
        time.sleep(1)
        t -= 1
    print("Time's up!")


while True:
    try:
        timeStr = input("Insert the time to count down (h:m:s): ")
        timeList = timeStr.split(":")
        for i in range(len(timeList)):
            timeList[i] = int(timeList[i])
        if (timeList[1] >= 60 or timeList[1] < 0) or (timeList[2] >= 60 or timeList[2] < 0):
            raise ValueError
        timeInSeconds = timeList[2] + timeList[1] * 60 + timeList[0] * 3600
        countdown(int(timeInSeconds))
        break
    except ValueError:
        print("Not a valid input. Make sure your input is in h:m:s format and m and s are integers between 0 and 59. ")
    except KeyboardInterrupt:
        print("Program stopped.")
        break
