from Memory import Memory
from Decoder import Decoder

class CPU:
    def __init__ (self, memory=None):
        self.AC = 0
        self.PC = 0
        self.RS = 0
        self.IR = 0
        self.MAR = 0
        self.MDR = 0

        self.C = False
        self.N = False
        self.Z = False
        self.V = False

        self.memory = memory
        if not memory:
            self.memory = Memory (255)
        
        self.isRunning = False
    
    def run (self):
        self.isRunning = True

        while (self.isRunning):
            self.search()
            self.decode()
            self.execute()
        
    def search (self):
        self.MAR = self.PC

        self.MDR = self.memory.get(self.MAR)
        self.PC += 1

        self.IR = self.MDR

        self.MAR = self.PC

        self.MDR = self.memory.get (self.MAR)
    
    def decode (self):
        #Instrução em IR e operando em MDR
        self.IR, addr = Decoder.DecomposeInstriction (self.IR)

        if self.IR not in [0x0, 0xd, 0xf]:
            self.PC += 1

        if addr == 0x1:
            self.MDR = self.memory.get (self.MDR)
        elif addr == 0x2:
            pointer = self.memory.get (self.MDR)
            self.MDR = self.memory.get (pointer)
        elif addr == 0x3:
            self.MDR = self.memory.get (self.MDR + self.PC)
    
    def execute (self):
        if self.IR >> 1 == 0x0:
            self.NOT ()
        
        elif self.IR >> 1 == 0x1:
            self.STA ()
        
        elif self.IR == 0x4:
            self.LDA ()

        elif self.IR == 0x5:
            self.ADD ()

        elif self.IR == 0x8:
            self.JMP ()

        elif self.IR == 0x9:
            self.JC ()

        elif self.IR == 0xa:
            self.JN ()

        elif self.IR == 0xb:
            self.JZ ()
        
        elif self.IR == 0xc:
            self.JSR ()

        elif self.IR == 0xd:
            self.RTS ()

        elif self.IR == 0xe:
            self.JV ()
        
        elif self.IR == 0xf:
            self.HLT ()

        self.UpdateFlags()
    
    def UpdateFlags(self):
        self.N = self.AC < 0
        self.Z = self.AC == 0
        self.C = self.AC >> 8 != 0x0

        self.V = False
        if self.AC > 0xff:
            self.AC = self.AC & 0xff
            self.V = True

    def NOT (self):
        self.AC = ~self.AC
    
    def STA (self):
        self.memory.set (self.MDR, self.AC)
    
    def LDA (self):
        self.AC = self.MDR
    
    def ADD (self):
        self.AC += self.MDR
    
    def JMP (self):
        self.PC = self.MDR
    
    def JC (self):
        self.PC = self.MDR if self.C else self.PC
    
    def JN (self):
        self.PC = self.MDR if self.N else self.PC

    def JZ (self):
        self.PC = self.MDR if self.Z else self.PC
    
    def JSR (self):
        self.RS = self.PC
        self.PC = self.MDR
    
    def RTS (self):
        self.PC = self.RS

    def JV (self):
        self.PC = self.MDR if self.V else self.PC
    
    def HLT (self):
        self.isRunning = False
        
    def __str__ (self):
        out =  " AC: {} \t\t\t C:{}\n".format (hex(self.AC), self.C)
        out += " PC: {} \t\t\t N:{}\n".format (hex(self.PC), self.N)
        out += " RS: {} \t\t\t Z:{}\n".format (hex(self.RS), self.Z)
        out += "MAR: {} \t\t\t V:{}\n".format (hex(self.MAR), self.V)
        out += "MDR: {} \t\t\t     \n".format (hex(self.MDR))
        out += " IR: {} \t\t\t       ".format (hex(self.IR))

        return out