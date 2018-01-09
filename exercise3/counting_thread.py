""" 
Thread used to count the time 
"""
import threading
import datetime

class CountingThread(threading.Thread):
    def __init__(self, master, start_time, end_time):
        super().__init__()
        self.master = master
        self.start_time = start_time
        self.end_time = end_time
        self.end_now = False
        self.paused = False
        self.force_quit = False

    def run(self):
        while True:
            if not self.paused and not self.end_now and not self.force_quit:
                self.main_loop()
                if datetime.datetime.now() >= self.end_time:
                    if not self.force_quit:
                        self.master.finish()
                        break
            elif self.end_now:
                self.master.finish()
                break
            elif self.force_quit:
                del self.master.worker
                return
            else:
                continue
        return

    def main_loop(self):
        now = datetime.datetime.now()
        if now < self.end_time:
            time_difference = self.end_time - now
            mins, secs = divmod(time_difference.seconds, 60)
            time_string = "{:02d}:{:02d}".format(mins, secs)
            if not self.force_quit:
                self.master.update_time_remaining(time_string)
