# my_set.py

class ListSet():

    def __init__(self):
        self.items = []

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items
        

    def __str__(self):
        return "Set of " + str(len(self.items)) + " elements"  

    def add(self, item):
        if not item in self.items:
            self.items.append(item)
            
    def union(self, other): 
        result = ListSet() 
        for item in self: 
            result.add(item) 
        for item in other: 
            result.add(item) 
        return result 

    def intersection(self, other):
        result = ListSet()
        for item in self:
            if item is other:
                result.add(item)
        return result

    def remove(self, item):
        self.items.remove(item)

if __name__ == "__main__" :
    a = ListSet()
    a.add(1)
    a.add(5.3)
    a.add("Hi")
    print(len(a))
    print (a)
    t = ListSet()
    t.add(3)
    t.add(10)
    t.add(1)
    b = a.union(t)
    print(b)
    c = a.intersection(t)
    print(c)
