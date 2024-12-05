import time
import threading
import subprocess
import time
from playsound import playsound


def main():
    while True:
        interval = 2 # Sets repeating interval in seconds
        sound_file = "./wave_sounds.wav"  # Path to your sound file
        print(f"Starting a timer that repeats every {interval} seconds.")
        

        with open("fadeout_from_cur_vol.applescript", "r") as script_file:
            fadeout_script = script_file.read()
            
        with open("fadein_to_desired_vol.applescript", "r") as script_file:
            fadein_script = script_file.read()
            
        with open("pause_spotify_or_music.applescript", "r") as script_file:
            pause_script = script_file.read()
            
        with open("play_spotify_or_music.applescript", "r") as script_file:
            play_script = script_file.read()
        

        time.sleep(interval)
        print("Interval over!")
        
        result = subprocess.run(["osascript", "-e", fadeout_script], text=True, capture_output=True)
        prev_vol = result.stdout.strip()
        subprocess.run(['osascript', '-e', pause_script, str(prev_vol)])
        
        playsound(sound_file)

        subprocess.run(['osascript', '-e', play_script])
        subprocess.run(['osascript', '-e', fadein_script, str(prev_vol)])


if __name__ == "__main__":
    main()
