import time
import subprocess

import snaps

current_time = time.localtime()

hour = current_time.tm_hour
minute = current_time.tm_min

if (hour>7) or (hour==7 and minute>29):
    # try snaps.display_message, otherwise fallback to printing
    try:
        snaps.display_message('TIME TO GET UP')
    except AttributeError:
        print('TIME TO GET UP')

    # try snaps.play_sound, otherwise use macOS afplay
    try:
        snaps.play_sound('siren.wav')
    except AttributeError:
        # afplay is available on macOS; use subprocess to play the file
        try:
            subprocess.Popen(['afplay', 'siren.wav'])
        except FileNotFoundError:
            print('Cannot play siren.wav: afplay not found')

    # pause the program to give the sound time to play
    time.sleep(10)