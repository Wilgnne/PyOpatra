from CPU import CPU
from time import sleep
import CLI

cpu = CPU ()

cpu.memory.setFromFile("C:\Cleo Simulator\examples\XOR.CLE")

cpu.isRunning = True
while (cpu.isRunning):
    
    CLI.clear ()
    print (cpu)
    print(hex(cpu.memory.get(cpu.PC)))
    print(hex(cpu.memory.get(cpu.PC+1)))
    input()
    cpu.search()

    cpu.decode()

    cpu.execute()
    
