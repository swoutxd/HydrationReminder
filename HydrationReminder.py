import winsound
import time

def reminder():
    for x in range(5):
        winsound.Beep(500,500)
    winsound.PlaySound("HydrationSound.wav", winsound.SND_ASYNC)
times_reminded = 0

while times_reminded < 5:
    times_reminded = times_reminded + 1
    reminder()
    print("Time to hydrate! Times reminded: " + str(times_reminded))
    time.sleep(5400)
