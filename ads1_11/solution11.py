''' Lesson 11 solution. '''

class BloomFilter:
    ''' Classic Bloom filter realisation. '''
    def __init__(self, f_len : int):
        self.filter_len : int = f_len
        self._filter : int = 0


    def hash1(self, str1 : str) -> int:
        ''' Returns slot for given key. Uses 17 as random number. '''
        pos : int = 0
        for c in str1:
            code : int = ord(c)
            pos = (pos * 17 + code) % self.filter_len
        return pos

    def hash2(self, str1 : str) -> int:
        ''' Returns slot for given key. Uses 223 as random number. '''
        pos : int = 0
        for c in str1:
            code : int = ord(c)
            pos = (pos * 223 + code) % self.filter_len
        return pos

    def add(self, str1 : str) -> None:
        ''' Adds given key in the filter (set all bits in
            all positions from hash-functions in 1). '''
        self._filter |= (2 ** self.hash1(str1)) | (2 ** self.hash2(str1))

    def is_value(self, str1 : str) -> bool:
        ''' Returns True if given key already exsists.
            Can give false-positive result. '''
        return self._filter & (2 ** self.hash1(str1)) and self._filter & (2 ** self.hash2(str1))





