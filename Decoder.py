class Decoder:

    @staticmethod
    def DecomposeInstriction (code:int) -> (int, int):
        instruc = code >> 4
        addr = (code & 0x0f) >> 2

        return instruc, addr