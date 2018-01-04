""" 
Virtual Operative System Scheduler 
"""
from threading import Thread


class Scheduler:
    
    # Scheduler APIs           
    def start_thread(self, thread_function, thread_arguments):    
        thread = Thread(target = thread_function, args = thread_arguments)
        thread.start()
        

    # Scheduler Constructor
    def __init__(self):
        print ("Initialize scheduler")
