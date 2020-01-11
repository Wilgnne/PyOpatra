class Memory:

    def __init__ (self, size):
        self.size = size
        self.mem = [0 for i in range (size)]
    
    def setFromFile(self, file:str):
        f = open(file, "rb")
        content = list (f.read ())
        for i in range (len (content)):
            self.set (i, content[i])
    
    def set (self, index:int, value:int):
        self.mem[index] = value
    
    def get (self, index:int):
        if (index < self.size):
            return self.mem[index]
        return 0