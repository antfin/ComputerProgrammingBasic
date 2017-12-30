""" 
Virtual Microcontroller Debugger:
- debug functions to print the status of all the 
  microcontroller registers and memory data
"""

class Debugger:    
    
    def print_registers(self, index = None):
        if (index == None):
            print("CPU Registers:")
            for i in range(0, self.cpu.REGISTER_NUM):                
                print("\t- Register {} = {}".format(i, self.cpu.REGISTER[i]))
        else:
            print("\t- Register {} = {}".format(index, self.cpu.REGISTER[index])) 
                           
    def print_data(self, address = None):
        if (address == None):
            print("CPU Data Memory")
            for i in range(0, self.cpu.DATA_MEMORY_SIZE_BYTE):
                print("\t- Address {} = {}".format(i, self.cpu.DATA_MEMORY[i])) 
        else:            
            print("\t- Address {} = {}".format(address, self.cpu.DATA_MEMORY[address])) 
    
    def print_overflow_flag(self):        
        print("CPU Overflow Flag = {}".format(self.OVERFLOW_BIT)) 
         
         
    # Debugger Constructor
    def __init__(self, cpu):        
        self.cpu = cpu
        return
        
