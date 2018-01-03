#!/usr/bin/env python
"""
Run the shell of the virtual OS and try to execute all 
the commands (use "help" to list all the available commands)  
"""

import operativesystem


def main(os):
    # Run OS shell
    os.shell()


if __name__ == '__main__':
    os = operativesystem.OperativeSystem()
    main(os)
        