""" 
Virtual Operative System Driver
"""
import time
import os


class Driver:      
      
    # Driver APIs
    def read_input(self, prompt=None):
        if prompt != None:
            text = input(prompt)
        else:
            text = input()
        return text 
    
    def write_output(self, text):
        print(text) 
        
    def log_error(self, text):
        print("<ERROR: " + text + ">") 
                
    def wait_time(self, seconds):
        time.sleep(seconds)   
        
    def clear_screen(self):
        if (os.name == 'nt'):
            os.system('cls')
        else:
            os.system('clear') 
        
    def shutdown(self):
        exit(1)
        
            
    # OperativeSystem Constructor
    def __init__(self):
        print ("Initialize drivers")          
