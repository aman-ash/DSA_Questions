# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# 1. What was the average temperature in first week of Jan
# 2. What was the maximum temperature in first 10 days of Jan

import pandas as pd

file = pd.read_csv('nyc_weather.csv')
print(file)


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
for i in range(file.shape[0]):
    ht[file['date'][i]] = file['temperature(F)'][i]

print(ht['Jan 9'])

print(min(ht.arr))
