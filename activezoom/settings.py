import tkinter as tk
from tkinter import ttk

from activezoom.toggledframe import ToggledFrame

PAD_X=10

class SettingsWindow():
    schedule_opts = ('Everday', 'Weekdays')
    time_range = ['%s:%s%s' % (h, m, ap) for ap in ('am', 'pm') for h in ([12] + list(range(1,12))) for m in ('00', '30')]
    time_range.append("Midnight")

    ex_difficulty = ('Beginner', 'Intermediate', 'Advanced')
    ex_types = ('Stretches', 'Bodyweight', 'Barbell', 'Dumbbells', 'Kettlebells')    

    def __init__(self, main_window):
        self.main_window = main_window
        
        # Create Toggle Window
        self.setting_win = ToggledFrame(main_window, text='Settings', relief="raised", borderwidth=1)
        self.setting_win.pack(fill="x", expand=1, pady=2, padx=2, anchor="s")

        # Notification Time Frame
        self.sched_frame = tk.Frame(self.setting_win.sub_frame)
        self.sched_frame.pack(fill="x", expand=1)
        ttk.Label(self.sched_frame, text='Notification schedule:').pack(side="left", padx=PAD_X)
        self.frequency = ttk.Combobox(self.sched_frame, values=self.schedule_opts, state='readonly')
        self.frequency.current(0)
        self.frequency.pack(side="left")

        self.start = ttk.Combobox(self.sched_frame, values=self.time_range, state='readonly')
        self.start.current(0)
        self.start.pack(side="left")

        ttk.Label(self.sched_frame, text=' to ').pack(side="left")

        self.end = ttk.Combobox(self.sched_frame, values=self.time_range, state='readonly')
        self.end.current(len(self.time_range) - 1)
        self.end.pack(side="left")

        ttk.Label(self.setting_win.sub_frame, text='---------------------------------------------------').pack()

        # Exercise Difficuly
        self.diff_frame = tk.Frame(self.setting_win.sub_frame)
        self.diff_frame.pack(fill="x", expand=1)
        ttk.Label(self.diff_frame, text='Exercise Difficulty:').pack(side="left", padx=PAD_X)
        self.frequency = ttk.Combobox(self.diff_frame, values=self.ex_difficulty, state='readonly')
        self.frequency.current(0)
        self.frequency.pack(side="left")

        ttk.Label(self.setting_win.sub_frame, text='---------------------------------------------------').pack()

        # Exercise Types
        self.type_frame = tk.Frame(self.setting_win.sub_frame)
        self.type_frame.pack(fill="x", expand=1)
        ttk.Label(self.type_frame, text='Exercise Types:').pack(side="left", padx=PAD_X)

        self.type_vals = []
        self.type_box = []
        for exercise in self.ex_types:
            self.type_vals.append(tk.BooleanVar())
            if(exercise == "Stretches" or exercise == "Bodyweight"):
                self.type_vals[-1].set(True)
            
            print(self.type_vals[-1].get())
            self.type_box.append(tk.Checkbutton(self.type_frame, text=exercise, variable=self.type_vals[-1], onvalue=True, offvalue=False))
            
            self.type_box[-1].pack(side="left")


        


