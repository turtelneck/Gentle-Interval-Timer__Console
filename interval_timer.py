import time
import subprocess
from playsound import playsound
import threading


def fade_pause_plays(fadeout, pause, play, fadein, nature_sound):
    # print("Interval over, fading out music")
    prev_vol = subprocess.run(["osascript", "-e", fadeout], text=True, capture_output=True)
    prev_vol_stripped = prev_vol.stdout.strip()

    # print("Pausing music...")
    result = subprocess.run(['osascript', '-e', pause, str(prev_vol_stripped)], text=True, capture_output=True)
    was_playing = result.stdout.strip().lower() == "true"

    playsound(nature_sound)

    # only required if music was playing previously
    # pause already sets volume back at normal levels
    if was_playing:
        print("We're in here for some reason??????\n")
        # print("Unpausing music...")
        subprocess.run(['osascript', '-e', play])

        # print("Fading music in")
        subprocess.run(['osascript', '-e', fadein, str(prev_vol_stripped)])


def timer(interval_seconds, interval_count, nature_sound, fadeout, pause, play, fadein):
    mins = interval_seconds // 60
    sec = interval_seconds - mins * 60
    
    print(f'{mins} min, {sec} sec timer, repeats for {interval_count} intervals\n')
    time.sleep(interval_seconds) # first timer runs outside loop
    
    for _ in range(interval_count - 1):
        print(f'{mins} min, {sec} sec timer, repeats for {interval_count} more intervals\n')
        start_time = time.time()
        
        fade_thread = threading.Thread(target=fade_pause_plays, args=(fadeout, pause, play, fadein, nature_sound,))
        fade_thread.start()
        fade_thread.join() # ensures timer never outpaces fade_pause_play
        
        # timer waits for time remaining, accounting for fade_pause_play execution time
        elapsed_time = time.time() - start_time
        print(f'{mins} min, {sec} sec timer beginning, repeats for {interval_count} intervals\n')
        # print(elapsed_time)
        time_to_wait = max(0, interval - elapsed_time)
        # print(time_to_wait)
        time.sleep(time_to_wait)
    
    fade_thread = threading.Thread(target=fade_pause_plays, args=(fadeout, pause, play, fadein, nature_sound,))
    fade_thread.start()
    fade_thread.join()


def main():
    with open("fadeout_from_cur_vol.applescript", "r") as script_file:
        fadeout = script_file.read()
    with open("fadein_to_desired_vol.applescript", "r") as script_file:
        fadein = script_file.read()
    with open("pause_spotify_or_music.applescript", "r") as script_file:
        pause = script_file.read()
    with open("play_spotify_or_music.applescript", "r") as script_file:
        play = script_file.read()
    
    user_minutes = float(input("Desired minutes per loop: "))
    interval_seconds = int(user_minutes * 60)
    interval_count = int(input("Desired number of timer repetitions: "))
    nature_sound = "./wave_sounds.wav"
    
    timer_thread = threading.Thread(target=timer, args=(interval_seconds, interval_count, nature_sound, fadeout, pause, play, fadein))
    timer_thread.start()
    timer_thread.join()

if __name__ == "__main__":
    main()


# BUGS:
# if volume starts muted, fadeout AppleScript divides by zero (not fatal)

# TO DO:
# check if music was playing before fading out, instead of during the pause script
# add the ability to kill the timer and restart with typed commands, possibly via threading?
