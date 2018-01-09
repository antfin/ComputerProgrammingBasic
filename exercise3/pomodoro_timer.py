""" 
Pomodoro Timer Application 
"""
import datetime
import sqlite3
import tkinter as tk
from tkinter import messagebox as msg
import config
import log_window
import counting_thread

class PomodoroTimer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config = config.Config()
        self._initMenuBar()
        self._initTaskName()
        self._initTimer()
        self._initButtons()
        self._initShortcut()
        self._configureDestroy()

    def _initMenuBar(self):
        self.title("Pomodoro Timer")
        self.geometry("500x350")
        self.resizable(False, False)
        self.standard_font = (None, 16)
        self.menubar = tk.Menu(self, bg=self.config.data["Colors"]["BackGround"], fg=self.config.data["Colors"]["ForeGround"])
        self.log_menu = tk.Menu(self.menubar, tearoff=0, bg=self.config.data["Colors"]["BackGround"], fg=self.config.data["Colors"]["ForeGround"])
        self.log_menu.add_command(label=self.config.data["String"]["Menu_DropDown_1_Item_1"], command=self._show_log_window, accelerator="Ctrl+L")
        self.menubar.add_cascade(label=self.config.data["String"]["Menu_DropDown_1"], menu=self.log_menu)
        self.configure(menu=self.menubar)
        self.main_frame = tk.Frame(self, width=500, height=350, bg=self.config.data["Colors"]["BackGround"])

    def _initTaskName(self):
        self.task_name_label = tk.Label(self.main_frame, text=self.config.data["String"]["Label_1"], bg=self.config.data["Colors"]["BackGround"], fg=self.config.data["Colors"]["ForeGround"], font=self.standard_font)
        self.task_name_label.pack(fill=tk.X, pady=15)
        self.task_name_entry = tk.Entry(self.main_frame, bg="white", fg=self.config.data["Colors"]["ForeGround"], font=self.standard_font)
        self.task_name_entry.pack(fill=tk.X, padx=50, pady=(0,20))

    def _initTimer(self):
        self.time_remaining_var = tk.StringVar(self.main_frame)
        self.time_remaining_value = "25:00"
        self.time_remaining_var.set(self.time_remaining_value)
        self.time_remaining_label = tk.Label(self.main_frame, textvar=self.time_remaining_var, bg=self.config.data["Colors"]["BackGround"], fg=self.config.data["Colors"]["ForeGround"], font=(None, 40))
        self.time_remaining_label.pack(fill=tk.X ,pady=15)  
        
    def _initButtons(self):
        self.start_button = tk.Button(self.main_frame, text=self.config.data["String"]["Button_1"], bg=self.config.data["Colors"]["BackGround"], fg=self.config.data["Colors"]["ForeGround"], command=self._start, font=self.standard_font)
        self.start_button.pack(fill=tk.X, padx=50)
        self.pause_button = tk.Button(self.main_frame, text=self.config.data["String"]["Button_3"], bg=self.config.data["Colors"]["BackGround"], fg=self.config.data["Colors"]["ForeGround"], command=self._pause, font=self.standard_font, state="disabled")
        self.pause_button.pack(fill=tk.X, padx=50)        
        #TODO: Insert break/pomodoro button 
        self.main_frame.pack(fill=tk.BOTH, expand=1)

    def _initShortcut(self):
        self.bind("<Control-l>", self._show_log_window)
        
    def _configureDestroy(self):
        self.protocol("WM_DELETE_WINDOW", self._safe_destroy)
        
    def _changeBreakTime(self):        
        #TODO: configure Break button callback
        print("<ERROR>: Not implemented")
        
    def _changePomodoroTime(self):
        #TODO: configure Pomodoro button callback
        print("<ERROR>: Not implemented")

    def _start(self):
        if not self.task_name_entry.get():
            msg.showerror("No Task", "Please enter a task name")
            return
        if not hasattr(self, "worker"):
            self._setup_worker()
        self.task_name_entry.configure(state="disabled")
        self.start_button.configure(text=self.config.data["String"]["Button_2"], command=self._finish_early)
        self.time_remaining_var.set(self.time_remaining_value)
        self.pause_button.configure(state="normal")
        self._add_new_task()
        self.task_finished_early = False
        self.worker.start()

    def _pause(self):
        self.worker.paused = not self.worker.paused
        if self.worker.paused:
            self.pause_button.configure(text=self.config.data["String"]["Button_4"])
            self.worker.start_time = datetime.datetime.now()
        else:
            self.pause_button.configure(text=self.config.data["String"]["Button_3"])
            end_timedelta = datetime.datetime.now() - self.worker.start_time
            self.worker.end_time = self.worker.end_time + datetime.timedelta(seconds=end_timedelta.seconds)

    def _finish_early(self):
        self.start_button.configure(text=self.config.data["String"]["Button_1"], command=self._start)
        self.task_finished_early = True
        self.worker.end_now = True

    def finish(self):
        self.task_name_entry.configure(state="normal")
        self.time_remaining_var.set(self.time_remaining_value)
        self.pause_button.configure(text=self.config.data["String"]["Button_3"], state="disabled")
        self.start_button.configure(text=self.config.data["String"]["Button_1"], command=self._start)
        if not self.task_finished_early:
            self._mark_finished_task()
        del self.worker
        msg.showinfo("Pomodoro Finished!", "Task completed, take a break!")

    def _setup_worker(self):
        now = datetime.datetime.now()
        in_25_mins = now + datetime.timedelta(minutes=int(self.time_remaining_value.split(":")[0]))
        #in_25_mins = now + datetime.timedelta(seconds=3)
        worker = counting_thread.CountingThread(self, now, in_25_mins)
        self.worker = worker
        
    def update_time_remaining(self, time_string):
        self.time_remaining_var.set(time_string)
        self.update_idletasks()

    def _add_new_task(self):
        task_name = self.task_name_entry.get()
        self.task_started_time = datetime.datetime.now()
        add_task_sql = "INSERT INTO pymodoros VALUES (?, 0, ?)"
        self.runQuery(add_task_sql, (task_name, self.task_started_time))

    def _mark_finished_task(self):
        task_name = self.task_name_entry.get()
        add_task_sql = "UPDATE pymodoros SET finished = ? WHERE task = ? and date = ?"
        self.runQuery(add_task_sql, ("1", task_name, self.task_started_time))

    def _show_log_window(self, event=None):
        log_window.LogWindow(self)

    def _safe_destroy(self):
        if hasattr(self, "worker"):
            self.worker.force_quit = True
            self.after(100, self._safe_destroy)
        else:
            self.destroy()

    @staticmethod
    def runQuery(sql, data=None, receive=False):
        conn = sqlite3.connect("pymodoro.db")
        cursor = conn.cursor()
        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)
        if receive:
            return cursor.fetchall()
        else:
            conn.commit()
        conn.close()

    @staticmethod
    def firstTimeDB():
        create_tables = "CREATE TABLE pymodoros (task text, finished integer, date text)"
        PomodoroTimer.runQuery(create_tables)
