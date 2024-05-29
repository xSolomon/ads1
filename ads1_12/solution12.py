''' Lesson 12 solution. '''

class NativeCache:
    ''' Cache realisation. '''
    def __init__(self, sz : int):
        self.size : int = sz
        self.step : int = 1
        self.slots : list[str] = [None] * self.size
        self.values : list = [None] * self.size
        self.hits : list[int] = [0] * self.size

    def hash_fun(self, key : str) -> int:
        ''' Applies hash-function to given string, resulting in correct index. 
            Hash = modulo size from bytesum of string. '''
        return sum(bytearray(key, encoding = 'utf8')) % self.size

    def put(self, key : str, value) -> None:
        ''' Adds value in the table at the given key.
            If no free slots found, adds at the index of key with least hits.
            If key already exists, rewrites value associated with it. '''
        pos : int = self.hash_fun(key)
        for _ in enumerate(self.slots):
            if self.slots[pos] is None or self.slots[pos] == key:
                self.slots[pos] = key
                self.values[pos] = value
                self.hits[pos] = self.hits[pos] + 1 if self.slots[pos] == key else 1
                return
            pos = (pos + self.step) % self.size
        least_hits_index : int = 0
        for i in range(1, self.size):
            if self.hits[i] < self.hits[least_hits_index]:
                least_hits_index = i
        self.hits[least_hits_index] = 1
        self.slots[least_hits_index] = key
        self.values[least_hits_index] = value

    def is_key(self, key : str) -> bool:
        ''' Returns True if given key is existing in table. '''
        pos : int = self.hash_fun(key)
        for _ in enumerate(self.slots):
            if self.slots[pos] == key:
                return True
            pos = (pos + self.step) % self.size
        return False

    def get(self, key : str):
        ''' Returns value associated with given key.
            Returns "None" if given key is not present. '''
        pos : int = self.hash_fun(key)
        for _ in enumerate(self.slots):
            if self.slots[pos] == key:
                self.hits[pos] += 1
                return self.values[pos]
            pos = (pos + self.step) % self.size
        return None








