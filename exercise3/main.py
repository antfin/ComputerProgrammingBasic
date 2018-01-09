#!/usr/bin/env python
"""
Add a new button to change the count down time:
-25 minutes pomodoro timeout
-5 minutes break timeout 

Based on https://github.com/Dvlv/Tkinter-By-Example 
"""
import os
import pomodoro_timer


def main(timer):
    # Run Pomodoro App
    if not os.path.isfile("pymodoro.db"):
        timer.firstTimeDB()
    timer.mainloop()
    
    
if __name__ == "__main__":
    timer = pomodoro_timer.PomodoroTimer()
    main(timer)
    