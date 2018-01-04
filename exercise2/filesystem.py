""" 
Virtual Operative System File System
"""
import os


class FileSystem:  
      
    # Settings    
    ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "root")  
            
            
    # FileSystem APIs     
    def list_files(self, directory_name):   
        files = [] 
        directory = os.path.join(self.ROOT, directory_name)
        if os.path.exists(directory): 
            for file in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, file)):
                    files.append("\t" + directory_name + "/" + file)
                else:
                    files.append("<DIR>\t" + directory_name + "/" + file)  
        return files        
    
    def read_file(self, file_name):           
        file = os.path.join(self.ROOT, file_name)
        if os.path.exists(file):  
            with open(file,'r') as file:
                data = file.read()
        else:
            data = None
        return data
        
    def write_file(self, file_name, data):           
        directory = os.path.dirname(os.path.join(self.ROOT, file_name))
        if os.path.exists(directory):
            file = open(os.path.join(self.ROOT, file_name), "w")
            file.write('\n'.join(data))
            file.close()
            return True
        else:
            return False
        
    def create_directory(self, directory_name):          
        new_directory = os.path.join(self.ROOT, directory_name)
        directory = os.path.dirname(new_directory)
        if os.path.exists(directory) and not os.path.exists(new_directory):
            os.makedirs(new_directory)
            return True
        else:
            return False
        
    
    # FileSystem Constructor
    def __init__(self):
        print ("Initialize file system")        
