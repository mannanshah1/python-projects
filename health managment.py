from pygame import mixer
from time import time
from _datetime import datetime

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops=-1, start=0.0, fade_ms=0)
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
if __name__ == '__main__':
    print("             ****************-Wellcome to Healthy Program-******************")
    print("Drink (0.5)liter of water every 30(min)\n""Eyes exercise every 30(min)\n""Physical Activity Every 45(min)")
    print("                        keep the program running to get reminders")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs =40*60
    exsecs = 30*60
    eyessecs = 45*60
    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            with open("water.txt", "a") as f:
                f.write("Drank water at " + ":" + str(datetime.now()) + "\n")
            print("logged successfully")

        if time() - init_eyes > eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            with open("eyes.txt", "a") as f:
                f.write("Done Eyes exercise at " + ":" + str(datetime.now()) + "\n")
            print("logged successfully")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            with open("physical.txt", "a") as f:
                f.write("Done Exercise at " + ":" + str(datetime.now()) + "\n")
            print("logged successfully")

