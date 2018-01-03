""" 
Virtual Operative System:
- 6 sync commands
- 1 async command simulating mutitasking
- virtual root file system 
"""
import time
import os
from threading import Thread


class OperativeSystem:
    
    # Settings    
    ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "root")  
    
    # OS commands    
    def _help_commands(self):
        print("Commands supported by pOS are:")    
        print("- help: list all the shell commands")
        print("- ls <DIRECTORY>: list all the files into the directory")
        print("- cat <FILENAME>: read a file")
        print("- vi <FILENAME>: write a file")
        print("- clear: clear the screen")
        print("- alarm #SECONDS: setup an alarm")
        print("- exit: terminate the shell")
        
    def _list_files(self, directory_name):    
        path = os.path.join(self.ROOT, directory_name)
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                print("\t" + directory_name + "/" + file)
            else:
                print("<DIR>\t" + directory_name + "/" + file)
        
    def _read_file(self, file_name):         
        file = os.path.join(self.ROOT, file_name)
        if os.path.exists(file):  
            with open(file,'r') as file:
                data = file.read()
            print(data)
        else:
            self._log_error("ERROR: File not Exist")
        
    def _write_file(self, file_name):
        lines = self._get_lines()
        file = open(os.path.join(self.ROOT, file_name), "w")
        file.write('\n'.join(lines))
        file.close()
                
    def _get_lines(self):
        print("Enter ':q' to end editing")
        lines = []
        line = input()
        while line != ':q':
            lines.append(line)
            line = input()
        return lines
        
    def _clear_screen(self):
        if (os.name == 'nt'):
            os.system('cls')
        else:
            os.system('clear')     
    
    def _set_alarm(self, seconds):    
        print("Setting alarm in " + seconds + "s")
        thread = Thread(target = self._threaded_sleep, args = (int(seconds), ))
        thread.start()
    
    def _threaded_sleep(self, seconds):
        time.sleep(seconds)    
        print("ALARM RING!!!")
        
    def _shutdown(self):
        print ("Shutting down..")
        exit(1)
            
    def _log_error(self, error):
        print(error)    
        
        
    def shell(self):
        self._clear_screen()
        while True:
            shell = input("> ")
            if (shell):
                words = shell.split()
                command = words[0]
                if command in self.COMMANDS:
                    if (len(words) == (self.COMMANDS[words[0]]["arguments_number"] + 1)):
                        action = self.COMMANDS[words[0]]["function"]
                        if (len(words) > 1):
                            argument = words[1].replace('/', '\\')
                            action(argument)
                        else:
                            action()
                    else:            
                        self._log_error("ERROR: Wrong argument number")
                else:
                    self._log_error("ERROR: " + command + " is not a recognized command")
        
    
    # OperativeSystem Constructor
    def __init__(self):
        print ("Boot pOs version 1.0")  
        self.COMMANDS = {
            'help' : {
                'function': self._help_commands,
                'arguments_number': 0
            }, 
            'ls' : {
                'function': self._list_files,
                'arguments_number': 1
            },
            'cat' : {
                'function': self._read_file,
                'arguments_number': 1
            },
            'vi' : {
                'function': self._write_file,
                'arguments_number': 1
            },
            'clear' : {
                'function': self._clear_screen,
                'arguments_number': 0
            },
            'alarm' : {
                'function': self._set_alarm,
                'arguments_number': 1
            },
            'exit' : {
                'function': self._shutdown,
                'arguments_number': 0
            }
        }   
        return
        
