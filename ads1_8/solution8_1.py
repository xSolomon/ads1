''' Lesson 8 solution. '''

class HashTable:
    ''' HashTable realistation. '''
    def __init__(self, sz, stp):
        self.size : int = sz
        self.step : int = stp
        self.slots : list[str] = [None] * self.size

    def hash_fun(self, value : str) -> int:
        ''' Applies hash-function to given string, resulting in correct index. 
            Hash = modulo size from bytesum of string. '''
        return sum(bytearray(value, encoding = 'utf8')) % len(self.slots)

    def seek_slot(self, value : str) -> int | None:
        ''' Tries to find free slot. First, assumes that free slot can be found
            via hash function. If not, performs search by formula:
            (pos + step) % size. If no available slots were found
            in len(HashTable) steps, returns "None". '''
        pos : int = self.hash_fun(value)
        for _ in enumerate(self.slots):
            if self.slots[pos] is None:
                return pos
            pos = (pos + self.step) % len(self.slots)
        return None

    def put(self, value : str) -> int | None:
        ''' Adds value in HashTable if any free slots.
            Returns index of that slot or None if no available slots. '''
        slot : int = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
        return slot

    def find(self, value : str) -> int | None:
        ''' Finds whether given value is presented in HashTable. 
            Returns corresponding slot or "None". '''
        pos : int =  self.hash_fun(value)
        for _ in enumerate(self.slots):
            if self.slots[pos] == value:
                return pos
            pos = (pos + self.step) % len(self.slots)
        return None






