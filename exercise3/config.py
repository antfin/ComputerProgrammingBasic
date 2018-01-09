"""
Read the config file
""" 

import os
import json


class Config:
    file_path = "config.json"
    data = {}
    
    def __init__(self):
        if os.path.isfile(self.file_path): 
            with open(self.file_path) as file:    
                self.data = json.load(file)    
    
