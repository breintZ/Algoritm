class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value  

class HashTable:
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * self.size
        self.count = 0
        
    def _hash(self, key):
        return abs(hash(key)) % self.size
    
    def __setitem__(self, key, value):
        if self.count < self.size:
            item = HashItem(key, value)
            h = self._hash(key)
            while self.slots[h] is not None:
                if self.slots[h].key is key:
                    break
                h = (h + 1) % self.size
            if self.slots[h] is None:
                self.count += 1
            self.slots[h] = item
            
    def __getitem__(self, key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size
            return None
        
if __name__ == "__main__" :
    ht = HashTable()
    print(ht.size, hash("good"), ht._hash("good"))
    ht["good"] = "eggs"
    ht["better"] = "ham"
    ht["best"] = "spam"
    ht["ad"] = "do not"
    ht["ga"] = "collide"
    for key in ("good", "better", "best", "worst", "ad", "ga"):
        v = ht[key]
        print(v)
    print("The number of elements is: {}".format(ht.count))
