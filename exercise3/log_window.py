""" 
Window that show all the pomodoro runs 
"""
import tkinter as tk
from tkinter import ttk

class LogWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self._initNotebook()
        dates = self._queryDates()
        for date in dates:            
            self._addTab(date)
        self._packNotebook()
                  
    def _initNotebook(self):
        self.title("Log")
        self.geometry("600x300")
        self.notebook = ttk.Notebook(self)
                
    def _queryDates(self):
        dates_sql = "SELECT DISTINCT date FROM pymodoros ORDER BY date DESC"
        dates = self.master.runQuery(dates_sql, None, True)
        for index, date in enumerate(dates):
            dates[index] = date[0].split()[0]
        dates = sorted(set(dates), reverse=True)
        return dates
    
    def _addTab(self, date):
        tab = self._initTab()
        tree = self._initTree(tab)
        self._addTasks(tree, date)          
        self._packTab(tab, date)
        
    def _packNotebook(self):
        self.notebook.pack(fill=tk.BOTH, expand=1)
        
    def _initTab(self):
        tab = tk.Frame(self.notebook)
        return tab
        
    def _initTree(self, tab):
        columns = ("name", "finished", "time")
        tree = ttk.Treeview(tab, columns=columns, show="headings")
        tree.heading("name", text="Name")
        tree.heading("finished", text="Full 25 Minutes")
        tree.heading("time", text="Time")
        tree.column("name", anchor="center")
        tree.column("finished", anchor="center")
        tree.column("time", anchor="center")
        return tree
        
    def _addTasks(self, tree, date):
        tasks = self._queryTasks(date)
        self._addTasksIntoTree(tree, tasks) 
        
    def _queryTasks(self, date):
        tasks_sql = "SELECT * FROM pymodoros WHERE date LIKE ?"
        date_like = date + "%"
        data = (date_like,)
        tasks = self.master.runQuery(tasks_sql, data, True)
        return tasks
    
    def _addTasksIntoTree(self, tree, tasks):
        for task_name, task_finished, task_date in tasks:
            task_finished_text = "Yes" if task_finished else "No"
            task_time = task_date.split()[1]
            task_time_pieces = task_time.split(":")
            task_time_pretty = "{}:{}".format(task_time_pieces[0], task_time_pieces[1])
            tree.insert("", tk.END, values=(task_name, task_finished_text, task_time_pretty))
        tree.pack(fill=tk.BOTH, expand=1)          
        
    def _packTab(self, tab, date):
        self.notebook.add(tab, text=date)
        