# Hash function implementing ASCII value
# def getHash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100

class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self, key) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.getHash(key)
        found = False
        # Updation
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        # First time insertion - When the key doesn't exists
        if not found:
            self.arr[h].append((key, value)) 

    def __getitem__(self, key):
        h = self.getHash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.getHash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

if __name__ == "__main__":
    ht = HashTable()
    
    ht['march 6'] = 130
    ht['march 6'] = 78
    ht['march 8'] = 67
    ht['march 9'] = 4
    ht['march 17'] = 459

    # del ht['march 6']

    print(ht.arr)

    # print(ht['march 17'])
    del ht['march 17']
    
    print(ht.arr)
