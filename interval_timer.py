import time
import subprocess
from playsound import playsound
import threading

with open("fadeout_from_cur_vol.applescript", "r") as script_file:
    fadeout_script = script_file.read()
with open("fadein_to_desired_vol.applescript", "r") as script_file:
    fadein_script = script_file.read()
with open("pause_spotify_or_music.applescript", "r") as script_file:
    pause_script = script_file.read()
with open("play_spotify_or_music.applescript", "r") as script_file:
    play_script = script_file.read()


def fade_pause_play(sound_file_path):
    # print("Interval over, fading out music")
    prev_vol = subprocess.run(["osascript", "-e", fadeout_script], text=True, capture_output=True)
    prev_vol_stripped = prev_vol.stdout.strip()

    # print("Pausing music...")
    was_playing = subprocess.run(['osascript', '-e', pause_script, str(prev_vol_stripped)])

    print("Playing chosen sound file")
    playsound(sound_file)

    # only required if music was playing previously
    # pause_script already sets volume back at normal levels
    if was_playing:
        # print("Unpausing music...")
        subprocess.run(['osascript', '-e', play_script])

        # print("Fading music in")
        subprocess.run(['osascript', '-e', fadein_script, str(prev_vol_stripped)])


def timer(interval_seconds, interval_count, sound_file_path):
    time.sleep(interval_seconds) # first timer runs outside loop
    for _ in range(interval_count - 1):
        print("Interval loop complete, starting new loop")
        start_time = time.time()
        
        fade_thread = threading.Thread(target=fade_pause_play, args=(sound_file_path,))
        fade_thread.start()
        fade_thread.join() # ensures timer never outpaces fade_pause_play
        
        # timer waits for time remaining, accounting for fade_pause_play execution time
        elapsed_time = time.time() - start_time
        # print(elapsed_time)
        time_to_wait = max(0, interval - elapsed_time)
        # print(time_to_wait)
        time.sleep(time_to_wait)
    
    fade_thread = threading.Thread(target=fade_pause_play, args=(sound_file_path,))
    fade_thread.start()
    fade_thread.join()


def main():
    user_minutes = float(input("Desired minutes per loop: "))
    interval_seconds = int(user_minutes * 60)
    interval_count = int(input("Desired number of timer repetitions: "))
    sound_file = "./wave_sounds.wav"
    
    print(f"Starting a timer that repeats every {user_minutes} minutes.")
    timer_thread = threading.Thread(target=timer, args=(interval_seconds, interval_count, sound_file))
    timer_thread.start()
    timer_thread.join()

if __name__ == "__main__":
    main()


# BUGS:
# if volume starts muted, fadeout AppleScript divides by zero (not fatal)

# TO DO:
# check if music was playing before fading out, instead of during the pause script 
