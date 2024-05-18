''' Dynamic array realisation. '''

import ctypes

class DynArray:
    ''' Represents dynamic array. '''
    def __init__(self):
        self.count : int = 0
        self.capacity : int = 16
        self.array : ctypes.Array[ctypes.py_object] = self.make_array(self.capacity)

    def __len__(self) -> int:
        ''' Returns current ary length. '''
        return self.count

    def make_array(self, new_capacity : int) -> ctypes.Array[ctypes.py_object]:
        ''' Creates new memory block of given capacity and returns it. '''
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i : int) -> ctypes.py_object:
        ''' Returns object under i position.
            Raises IndexError if i is out of bounds. '''
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity : int) -> None:
        ''' Change internal buffer capacity and
            copy exising array into it. '''
        new_capacity = max(new_capacity, 16)
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm : ctypes.py_object) -> None:
        ''' Adds new element at the end of array. 
            If no free space, resizes internal buffer by 2 times. '''
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i : int, itm : ctypes.py_object) -> None:
        ''' Inserts object itm in i position, shifting elements to the right. 
            If i = count, appends itm in the tail. 
            Raises IndexError if i is out of bounds. '''
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        for j in range(self.count, i, -1):
            self.array[j] = self.array[j - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i : int) -> None:
        ''' Deletes object in i position, shrinking buffer if needed.
            Raises IndexError if i is out of bounds. '''
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]
        self.count -= 1
        if self.count * 2 < self.capacity:
            self.resize(int(self.capacity / 1.5))



