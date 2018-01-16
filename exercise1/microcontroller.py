""" 
Virtual Microcontroller:
- 10 Hz 
- 8 bits 
- 4 CPU registers
- 4 OpCodes: LD, ADD, DIV and ST
- 16 Byte data memory 
"""
import random
import time
import math
import debugger

class VirtualMicrocontroller:
    
    # Settings    
    FREQUENCY_HZ = 1000
    REGISTER_NUM = 4
    REGISTER_SIZE_BIT = 16 
    DATA_SIZE_BIT = 8 
    DATA_MEMORY_SIZE_BYTE = 16     
    
    # OpCodes
    def LD(self, source_register, destination_register):
        self.REGISTER[destination_register] = self.REGISTER[source_register]
        time.sleep(1/self.FREQUENCY_HZ)
        return
    
    def LD_A(self, address, register):
        self.REGISTER[register] = self.DATA_MEMORY[address]
        time.sleep(1/self.FREQUENCY_HZ)
        return
    
    def LD_N(self, number, register):        
        if (number < self.REGISTER_MAX_VALUE):
            self.OVERFLOW_BIT = 0
        else:
            self.OVERFLOW_BIT = 1
        self.REGISTER[register] = int(number % self.REGISTER_MAX_VALUE)
        time.sleep(1/self.FREQUENCY_HZ)        
        return    
    
    def ADD(self, first_register, second_register, result_register):
        number = self.REGISTER[first_register] + self.REGISTER[second_register]
        if (number < self.REGISTER_MAX_VALUE):
            self.OVERFLOW_BIT = 0
        else:
            self.OVERFLOW_BIT = 1
        self.REGISTER[result_register] = int(number % self.REGISTER_MAX_VALUE)
        time.sleep(1/self.FREQUENCY_HZ)  
        return    
    
    def DIV(self, first_register, second_register, result_register):        
        self.REGISTER[result_register] = int(self.REGISTER[first_register] / self.REGISTER[second_register])
        time.sleep(1/self.FREQUENCY_HZ)  
        return
    
    def ST(self, register, address):
        number = self.REGISTER[register]
        if (number < self.DATA_MAX_VALUE):
            self.OVERFLOW_BIT = 0
        else:
            self.OVERFLOW_BIT = 1
        self.DATA_MEMORY[address] = int(number % self.DATA_MAX_VALUE)
        time.sleep(1/self.FREQUENCY_HZ)
        return   
    
    # MicroController Constructor
    def __init__(self):        
        self.OVERFLOW_BIT = 0
        self.REGISTER_MAX_VALUE = math.pow(2, self.REGISTER_SIZE_BIT)
        self.REGISTER = [0 for x in range(self.REGISTER_NUM)]    
        self.DATA_MAX_VALUE = math.pow(2, self.DATA_SIZE_BIT)
        self.DATA_MEMORY = [random.randint(1, 10) for x in range(self.DATA_MEMORY_SIZE_BYTE)]
        #self.DATA_MEMORY = [random.randint(0, self.DATA_MAX_VALUE - 1) for x in range(self.DATA_MEMORY_SIZE_BYTE)]
        self.debugger = debugger.Debugger(self)
        return
        
