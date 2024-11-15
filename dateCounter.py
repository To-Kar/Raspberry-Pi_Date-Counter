import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import os
import locale
from ttkbootstrap import Style
class DateCounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Datum und Zeit")
        # Set German locale
        locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
        # Set font for the entire window
        self.master.option_add("*Font", "Helvetica 24")
        # Main frame
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(padx=0, pady=50)
         # Label to display current date and time
        self.date_time_label = ttk.Label(self.main_frame, font=('Helvetica', 24), wraplength=2000,
          width=300)
        self.date_time_label.pack(pady=20)
        # Label to display days left until the end of the year
        self.days_left_label = ttk.Label(self.main_frame, font=('Helvetica', 24), wraplength=600)
        self.days_left_label.pack(pady=20)
        # Button frame
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack()
        # Button to play sound
        self.sound_button = ttk.Button(self.button_frame, text="Klang abspielen",
        command=self.play_sound)
        self.sound_button.pack(ipady=20, ipadx=20) # Increase padding to make the button larger
        # Deaktiviere die Geometrieübertragung für das Button-Frame
        self.button_frame.grid_propagate(False)
        # Setze die Größe des Button-Frames
        self.button_frame.config(width=500, height=500)
        # Setze den Stil des Buttons
        self.style = ttk.Style()
        self.style.configure('My.TButton', font=('Helvetica', 20)) # Setze Schriftgröße des Buttons
        self.sound_button.configure(style='My.TButton')
        self.master.geometry("480x320")
        self.update_display()
        # Tastenkombination zum Wechseln zwischen Vollbild- und Normalmodus
        self.master.bind('<F11>', self.toggle_fullscreen)
        #Tastenkombination zum Beenden des Vollbildmodus (F12)
        self.master.bind('<F12>', self.exit_fullscreen)
        # Starte im Vollbildmodus
        self.toggle_fullscreen()



    def update_display(self):
        # Get current date and time
        now = datetime.now()
        formatted_date_time = now.strftime("%A, %d. %B %Y %H:%M:%S")
        # Update date and time label
        self.date_time_label.config(text=f"\t\t\t{formatted_date_time}", width=1000)
        # Calculate days left until the end of the year
        end_of_year = datetime(now.year, 12, 31)
        days_left = (end_of_year - now).days
        # Update days left label
        self.days_left_label.config(text=f"Tage bis zum Jahresende:\n{days_left}")
        # Schedule update every second
        self.master.after(1000, self.update_display)

        
    def play_sound(self):
        try:
            # Get current date and time
            now = datetime.now()
            day_of_year = now.strftime('%B_%d') # e.g., "January_01", "February_14", etc.
            sound_file = f"{day_of_year}.wav" # Change the extension if your sound files are different
            os.system(f"aplay {sound_file}") # For Linux, change this accordingly for other OS
        except Exception as e:
            print("Error playing sound:", e)
    def toggle_fullscreen(self, event=None):
        self.master.attributes('-fullscreen', not self.master.attributes('-fullscreen'))
    def exit_fullscreen(self, event=None):
        self.master.attributes('-fullscreen', False)
def main():
    root = tk.Tk()
    app = DateCounterApp(root)
    # Use ttkbootstrap style with 'darkly' theme
    style = Style('darkly')
    style.master.title('Datum und Zeit')
    root.mainloop() # Start the main event loop using root
if __name__ == "__main__":
    main()