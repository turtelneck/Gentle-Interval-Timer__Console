import tkinter as tk
from tkinter import messagebox
import threading
import time
from playsound import playsound

# Importing existing modules
import input_valid  # !!! Assumes these functions are adjusted for non-terminal use. Will need to fix.
import timer_controls  # Timer logic

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interval Timer")

        # Input fields
        tk.Label(root, text="Minutes per loop:").grid(row=0, column=0, padx=10, pady=5)
        self.minutes_entry = tk.Entry(root)
        self.minutes_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Number of repetitions:").grid(row=1, column=0, padx=10, pady=5)
        self.repetitions_entry = tk.Entry(root)
        self.repetitions_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.grid(row=2, column=0, padx=10, pady=10)

        self.cancel_button = tk.Button(root, text="Cancel Timer", command=self.cancel_timer, state=tk.DISABLED)
        self.cancel_button.grid(row=2, column=1, padx=10, pady=10)

        # Timer Status
        self.status_label = tk.Label(root, text="Timer status: Ready")
        self.status_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Thread Control
        self.timer_thread = None
        self.running = False

    def start_timer(self):
        try:
            # Validate and parse inputs
            minutes = float(self.minutes_entry.get())
            repetitions = int(self.repetitions_entry.get())

            if minutes <= 0 or repetitions <= 0:
                raise ValueError("Inputs must be positive numbers.")

            interval_seconds = int(minutes * 60)
            
            # Start the timer thread
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.cancel_button.config(state=tk.NORMAL)
            self.status_label.config(text="Timer running...")

            self.timer_thread = threading.Thread(
                target=self.run_timer, args=(interval_seconds, repetitions)
            )
            self.timer_thread.start()
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def cancel_timer(self):
        self.running = False
        self.status_label.config(text="Timer canceled.")
        self.start_button.config(state=tk.NORMAL)
        self.cancel_button.config(state=tk.DISABLED)

    def run_timer(self, interval_seconds, repetitions):
        try:
            for i in range(repetitions):
                if not self.running:
                    break

                mins, secs = divmod(interval_seconds, 60)
                self.status_label.config(
                    text=f"Running: {mins} minutes, {secs} seconds. Remaining: {repetitions - i} loops"
                )
                time.sleep(interval_seconds)  # Simulate interval

                # Play sound
                if self.running:
                    playsound("./wave_sounds.wav")

            if self.running:
                self.status_label.config(text="Timer completed!")
            else:
                self.status_label.config(text="Timer canceled.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

        # Reset buttons
        self.start_button.config(state=tk.NORMAL)
        self.cancel_button.config(state=tk.DISABLED)
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
