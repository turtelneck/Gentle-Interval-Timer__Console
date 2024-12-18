import time
import subprocess
from playsound import playsound


def fade_pause_play(player_check, fadeout, pause, play, fadein, nature_sound):
    result = subprocess.run(['osascript', '-e', player_check], text=True, capture_output=True)
    was_playing = result.stdout.strip().lower() == "true"
    
    if was_playing:
        result = subprocess.run(['osascript', '-e', fadeout], text=True, capture_output=True)
        prev_vol = result.stdout.strip()

        subprocess.run(['osascript', '-e', pause, str(prev_vol)])

    playsound(nature_sound)
    
    if was_playing:
        # prev_vol is captured separately here from above in case a user adjusts volume during playsound()
        result = subprocess.run(['osascript', '-e', play], text=True, capture_output=True)
        prev_vol = result.stdout.strip()

        subprocess.run(['osascript', '-e', fadein, str(prev_vol)])


def timer(interval_seconds, interval_count):
    with open("player_check.applescript", "r", encoding="utf-8") as script_file:
        player_check = script_file.read()
    with open("fadeout_from_cur_vol.applescript", "r", encoding="utf-8") as script_file:
        fadeout = script_file.read()
    with open("fadein_to_desired_vol.applescript", "r", encoding="utf-8") as script_file:
        fadein = script_file.read()
    with open("pause_spotify_or_music.applescript", "r", encoding="utf-8") as script_file:
        pause = script_file.read()
    with open("play_spotify_or_music.applescript", "r", encoding="utf-8") as script_file:
        play = script_file.read()
        
    nature_sound = "./wave_sounds.wav"

    mins = interval_seconds // 60
    sec = interval_seconds - mins * 60
    
    time.sleep(0.3)
    print('\nTO CANCEL: control^c')
    time.sleep(0.4)
    print('\nTimer Beginning')
    time.sleep(0.8)
    print(f'{mins} min, {sec} sec timer, repeats for {interval_count} intervals')
    time.sleep(interval_seconds) # first timer runs outside loop
    
    for _ in range(interval_count - 1):
        start_time = time.time()
        
        fade_pause_play(player_check, fadeout, pause, play, fadein, nature_sound)
        print(f'{mins} min, {sec} sec timer, repeats for {interval_count - _ - 1} more intervals\n')
        
        # timer waits for time remaining, accounting for fade_pause_play execution time
        elapsed_time = time.time() - start_time
        # print(elapsed_time)
        time_to_wait = max(0, interval_seconds - elapsed_time)
        # print(time_to_wait)
        time.sleep(time_to_wait)
    
    # final nature sound played outside loop
    fade_pause_play(player_check, fadeout, pause, play, fadein, nature_sound)
