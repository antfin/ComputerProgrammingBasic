#!/usr/bin/env python
"""
Using the virtual 10 Hz 8 bits Microcontroller with 4 registers, 
calculate the mean of the first 10 values of the Data Memory and 
store the results in the 11th Data Memory position
"""

import time
import microcontroller


def main(cpu):
    # Calculate the mean of the first 4 data
    # To be updated to calculate the meant of the first 10 data
    cpu.LD_A(0, 0)
    cpu.LD_A(1, 1)     
    cpu.ADD(0, 1, 0)
    cpu.LD_A(2, 1)
    cpu.ADD(0, 1, 0) 
    cpu.LD_A(3, 1)
    cpu.ADD(0, 1, 0)
    cpu.LD_N(4, 2)    
    cpu.DIV(0, 2, 3)
    cpu.ST(3, 10)    
    cpu.debugger.print_registers()


if __name__ == '__main__':
    start = time.time()
    cpu = microcontroller.VirtualMicrocontroller()
    cpu.debugger.print_data()
    main(cpu)
    end = time.time() 
    duration = end - start   
    print("Data Values Mean:")   
    cpu.debugger.print_data(10)      
    print("Execution Time = {}".format(duration)) 
    