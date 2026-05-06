class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity 
        

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        return 

    def pushback(self, n: int) -> None:
        if self.size  == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

        return 

    def popback(self) -> int:
        element = self.arr[self.size -1 ]
        self.size -=1
        return element


    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_arr = [0] * new_capacity
        for i in range(self.capacity):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity 
        return 

    def getSize(self) -> int:
        return self.size 
    
    def getCapacity(self) -> int:
        return self.capacity