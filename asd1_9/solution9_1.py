''' Lesson 9 solution. '''

class NativeDictionary:
    ''' Dictionary realisaton. '''
    def __init__(self, sz : int):
        self.size : int = sz
        self.step : int = 1
        self.slots : list[str] = [None] * self.size
        self.values : list = [None] * self.size

    def hash_fun(self, key : str) -> int:
        ''' Applies hash-function to given string, resulting in correct index. 
            Hash = modulo size from bytesum of string. '''
        return sum(bytearray(key, encoding = 'utf8')) % self.size

    def is_key(self, key : str) -> bool:
        ''' Returns True if given key is existing in table. '''
        pos : int = self.hash_fun(key)
        for _ in enumerate(self.slots):
            if self.slots[pos] == key:
                return True
            pos = (pos + self.step) % self.size
        return False

    def put(self, key : str, value) -> None:
        ''' Adds value in the table at the given key.
            If no free slots found, adds at the index from hash function.
            If key already exists, rewrites value associated with it. '''
        pos : int = self.hash_fun(key)
        for _ in enumerate(self.slots):
            if self.slots[pos] is None or self.slots[pos] == key:
                break
            pos = (pos + self.step) % self.size
        self.slots[pos] = key
        self.values[pos] = value

    def get(self, key : str):
        ''' Returns value associated with given key.
            Returns "None" if given key is not present. '''
        pos : int = self.hash_fun(key)
        for _ in enumerate(self.slots):
            if self.slots[pos] == key:
                return self.values[pos]
            pos = (pos + self.step) % self.size
        return None








