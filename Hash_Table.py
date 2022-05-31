class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


ht = HashTable()

ht['march 6'] = 130
ht['march 7'] = 230
ht['nov 7'] = 330
ht['march 9'] = 430
ht['march 10'] = 530
ht['dec 11'] = 630
ht['jan 12'] = 730
ht['march 13'] = 830
ht['june 24'] = 930

del ht['march 16']

print(ht['nov 7'])
