# TotalHorizons / 0horizon
# 2/13/2024

# Imports
import socket # Checking open ports
from time import sleep # Avoiding rate limits
from rich.console import Console # Styling
from rich import print as rprint # Styling
import os # //

console = Console() # Eases the use of Rich prints

# Classes/Functions
class PortScanner: 
    def singleCheck(self, ipAddress, port): # Check if a SINGLE port is open
        Target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            Target.connect((ipAddress, port)) # Connection test. If the connection is refused, it moves to the exception on line 17.
            return True 
        except Exception as e:
            return False
        
    def openPorts(self, ipAddress, portRange: int): # Checks the range of ports provided by the 
        Ports = []
        for i in range(1, (portRange + 1)):
            result = self.singleCheck(ipAddress, i) # Using the 1st function in the class to check the port
            if result:
                console.print(f"[green][bold][!][/bold] Port {i} is open.")
                Ports.append(i, Ports)
            else:
                console.print(f"[red][bold][!][/bold] Port {i} is closed.")
            sleep(0.3) # Cooldown
        if len(Ports) > 0:
            console.print(f"[green][!] Open ports:\n{Ports}")
        else:
            console.print(f"[red][!] No open ports found!")

class Menu:
    def getArgs(self):
        IP = input("IP Address: ")
        portRange = int(input("Port Range: "))
        return IP, portRange # Reutrning the input to be used in the main function

    def main(self):
        os.system("clear") # Clears the terminal for a cleaner look. Written with Linux systems in mind.
        console.print("[red][bold] Port Scanner", justify="center")
        console.print("[red][italic] Programmed by 0horizon", justify="center")
        return self.getArgs() # Returning args fetched from getArgs function
        
#Code
MenuClass = Menu()
PSClass = PortScanner()

if __name__ == "__main__":
    Args = MenuClass.main()
    IP = Args[0] # As the Args are returned as (IP, PortRange), we can use indexing to reference them
    PortRange = Args[1]

    if (len(IP) == 0) or (len(str(PortRange)) == 0) or (PortRange == 0): # Input validation
        console.print("[red][bold][!] One or more invalid input")
    else:
        try:
            PSClass.openPorts(IP, PortRange)
        except Exception as e:
            console.print(f"[yellow]{e}")
