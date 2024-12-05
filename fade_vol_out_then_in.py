import time
import subprocess
from playsound import playsound


with open("fadeout_from_cur_vol.applescript", "r") as script_file:
    fadeout_script = script_file.read()
with open("fadein_to_desired_vol.applescript", "r") as script_file:
    fadein_script = script_file.read()
with open("pause_spotify_or_music.applescript", "r") as script_file:
    pause_script = script_file.read()
with open("play_spotify_or_music.applescript", "r") as script_file:
    play_script = script_file.read()

interval_seconds = 2
interval_count = 2
sound_file = "wave_sounds.wav"


def timer(interval, sound_file_path):
    print("starting timer!")
    time.sleep(interval)
    
    print("interval over, fading out music")
    result = subprocess.run(["osascript", "-e", fadeout_script], text=True, capture_output=True)
    prev_vol = result.stdout.strip()
    
    print("pausing music...")
    subprocess.run(['osascript', '-e', pause_script, str(prev_vol)])
    
    print("playing chosen sound file")
    playsound(sound_file_path)
    
    print("unpausing music...")
    subprocess.run(['osascript', '-e', play_script])
    
    print("fading music in")
    subprocess.run(['osascript', '-e', fadein_script, str(prev_vol)])


def main():
    print(f"Starting a timer that repeats every {interval_seconds} seconds.")
    
    for _ in range(interval_count):
        timer(interval_seconds, sound_file)

            
if __name__ == "__main__":
    main()
