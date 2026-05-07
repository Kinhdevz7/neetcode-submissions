class DynamicArray:
    # O(N) N = capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 
        self.arr = [0] * self.capacity


    # O(1)
    def get(self, i: int) -> int:
        if i >= self.size:
             return -1
        return self.arr[i]

    # O(1)
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        return 

    # O(1) ammortized/Avg case
    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    # O(1)
    def popback(self) -> int:
        element = self.arr[self.size -1 ]
        self.size -=1
        return element

    # O(N)
    def resize(self) -> None:
        self.capacity *= 2 
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        
        return 

    # O(1)
    def getSize(self) -> int:
        return self.size
    # O(1)
    def getCapacity(self) -> int:
        return self.capacity