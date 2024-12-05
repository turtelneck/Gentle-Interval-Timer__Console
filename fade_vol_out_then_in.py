import subprocess
import time


with open("fadeout_from_cur_vol.applescript", "r") as script_file:
    fadeout_script = script_file.read()
    
with open("fadein_to_desired_vol.applescript", "r") as script_file:
    fadein_script = script_file.read()
    
with open("pause_spotify_or_music.applescript", "r") as script_file:
    pause_script = script_file.read()
    
with open("play_spotify_or_music.applescript", "r") as script_file:
    play_script = script_file.read()


result = subprocess.run(["osascript", "-e", fadeout_script], text=True, capture_output=True)
subprocess.run(['osascript', '-e', pause_script])

prev_vol = result.stdout.strip()
time.sleep(2)

subprocess.run(['osascript', '-e', play_script])
subprocess.run(['osascript', '-e', fadein_script, str(prev_vol)])
