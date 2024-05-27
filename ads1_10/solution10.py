''' Lesson 10 solution. '''

class PowerSet:
    ''' Set realisation. '''
    def __init__(self):
        self.set : dict = {}

    def size(self) -> int:
        ''' Returns current set length. '''
        return len(self.set)

    def put(self, value):
        ''' Adds value to the set. Does nothing if value is already present. '''
        self.set[value] = 1

    def get(self, value) -> bool:
        ''' Returns True if value is presented in current set. '''
        return value in self.set

    def remove(self, value) -> bool:
        ''' Returns True if value was removed from set. '''
        if value in self.set:
            self.set.pop(value)
            return True
        return False

    def intersection(self, set2) -> 'PowerSet':
        ''' Returns new set, which is intersection between current and given sets. '''
        result : PowerSet = PowerSet()
        for key in self.set:
            if key in set2.set:
                result.put(key)
        return result

    def union(self, set2) -> 'PowerSet':
        ''' Returns new set, which is union between current and given sets. '''
        result : PowerSet = PowerSet()
        for key in self.set:
            result.set[key] = 1
        for key in set2.set:
            result.set[key] = 1
        return result

    def difference(self, set2) -> 'PowerSet':
        ''' Returns new set, which is difference between current and given sets. '''
        result : PowerSet = PowerSet()
        for key in self.set:
            if key not in set2.set:
                result.set[key] = 1
        return result

    def issubset(self, set2) -> bool:
        ''' Returns True if given set is a subset of current set. '''
        return set2.set.items() <= self.set.items()





