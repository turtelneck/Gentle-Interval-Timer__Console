import time
import threading
from playsound import playsound  # Install with `pip install playsound`

# Timer function
def timer(interval, sound_file):
    while True:
        time.sleep(interval)
        print("Interval over!")  # Optional: Visual cue
        playsound(sound_file)

def main():
    interval = 20 # Sets repeating interval in seconds
    sound_file = "./wave_sounds.wav"  # Path to your sound file
    print(f"Starting a timer that repeats every {interval} seconds.")
    
    # Start timer in a separate thread to keep it unobtrusive
    timer_thread = threading.Thread(target=timer, args=(interval, sound_file))
    timer_thread.daemon = True  # Ensures the thread ends when the main program exits
    timer_thread.start()
    
    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        print("Timer stopped.")

if __name__ == "__main__":
    main()
