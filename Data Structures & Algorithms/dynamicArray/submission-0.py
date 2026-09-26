class DynamicArray:
    
    def __init__(self, capacity: int):
        # Max capacity of the backing array
        self.capacity = capacity
        # Number of elements currently stored (<= capacity)
        self.length = 0
        # Backing storage
        self.arr = [0] * capacity

    # Get value at i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    # Set value n at i-th index
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # Push n to the end of the array
    def pushback(self, n: int) -> None:
        # Double capacity if we're full
        if self.length == self.capacity:
            self.resize()
        # Place n at next empty slot and grow logical size
        self.arr[self.length] = n
        self.length += 1

    # Pop and return the last element
    def popback(self) -> int:
        # Shrink logical size, then return the removed element
        self.length -= 1
        return self.arr[self.length]

    # Double the capacity of the array
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
        # Copy only the used elements into the new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    # Return the number of elements in the array
    def getSize(self) -> int:
        return self.length
    
    # Return the current capacity of the array
    def getCapacity(self) -> int:
        return self.capacity