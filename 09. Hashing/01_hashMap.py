# Hash function implementing ASCII value
# def getHash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100

class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def getHash(self, key) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.getHash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.getHash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.getHash(key)
        self.arr[h] = None

if __name__ == "__main__":
    ht = HashTable()
    
    ht['march 6'] = 130
    ht['march 1'] = 10
    ht['dec 17'] = 27

    del ht['march 6']

    # print(ht.arr)

    print(ht['march 6'])
