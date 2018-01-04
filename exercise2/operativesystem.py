""" 
Virtual Operative System:
- 6 sync commands
- 1 async command simulating mutitasking
- virtual root file system 
"""
import time
import driver
import filesystem
import scheduler


class OperativeSystem:        
    # OS commands    
    def _help_commands(self):
        self.driver.write_output("Commands supported by pOS are:")    
        self.driver.write_output("- help: list all the shell commands")
        self.driver.write_output("- ls <DIRECTORY>: list all the files into the directory")
        self.driver.write_output("- cat <FILE_NAME>: read a file")
        self.driver.write_output("- vi <FILE_NAME>: write a file")
        self.driver.write_output("- mkdir <DIRECTORY_NAME>: create a new directory")
        self.driver.write_output("- clear: clear the screen")
        self.driver.write_output("- alarm <SECONDS>: setup an alarm")
        self.driver.write_output("- exit: terminate the shell")
        
    def _list_files(self, directory_name):
        files = self.filesystem.list_files(directory_name) 
        if files: 
            for file in files:
                    self.driver.write_output(file)
        else:
            self.driver.log_error("Directory not Exist")  
        
    def _read_file(self, file_name): 
        data = self.filesystem.read_file(file_name)  
        if data:  
            self.driver.write_output(data)
        else:
            self.driver.log_error("File not Exist")
        
    def _write_file(self, file_name):        
        lines = self._get_lines()
        result = self.filesystem.write_file(file_name, lines)  
        if result == False:
            self.driver.log_error("Directory not Exist")  
                       
    def _create_directory(self, directory_name):
        # Use file system APIs to create a new directory
        self.driver.log_error("Function not implemented")      
        
    def _clear_screen(self):
        self.driver.clear_screen()
        
    def _set_alarm(self, seconds):    
        self.driver.write_output("Setting alarm in " + seconds + "s")
        self.scheduler.start_thread(self._threaded_sleep, (int(seconds), ))
            
    def _shutdown(self):
        self.driver.write_output("Shutting down..")
        self.driver.shutdown()    
       
       
    def _get_lines(self):
        self.driver.write_output("Enter ':q' to end editing")
        lines = []
        line = self.driver.read_input()
        while line != ':q':
            lines.append(line)
            line = self.driver.read_input()
        return lines       
                     
    def _threaded_sleep(self, seconds):
        time.sleep(seconds)    
        self.driver.write_output("ALARM RING!!!")
        
         
    # OS shell    
    def shell(self):
        self._clear_screen()
        while True:
            shell = self.driver.read_input("> ")
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
                        self.driver.log_error("Wrong argument number")
                else:
                    self.driver.log_error(command + " is not a recognized command")
        
    
    # OperativeSystem Constructor
    def __init__(self):
        print("Boot pOs version 1.0")        
        self.driver = driver.Driver()
        self.filesystem = filesystem.FileSystem()
        self.scheduler = scheduler.Scheduler() 
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
            'mkdir' : {
                'function': self._create_directory,
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
