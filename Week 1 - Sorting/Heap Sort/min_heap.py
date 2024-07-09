class MinHeap:
    def __init__(self):
        self.arr = []

    def add(self, num):
        self.arr.append(num)

        # Fix order
        currIdx = len(self.arr) - 1
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and (self.arr[parentIdx] == None or self.arr[currIdx] < self.arr[parentIdx]):
            self.arr[currIdx], self.arr[parentIdx] = self.arr[parentIdx], self.arr[currIdx]
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    # Extract the minimum number
    def extract(self):
        if len(self.arr) == 0:
            return None
        extracted = self.arr[0]
        minIdx = 0
        currIdx = 0

        while True:
            minIdx = self.find_min_idx(currIdx)
            if minIdx == None:
                if currIdx == len(self.arr) - 1:
                    del self.arr[currIdx]
                    # Trim any other Nones to the left
                    lastIdx = currIdx - 1
                    while lastIdx >= 0 and self.arr[lastIdx] == None:
                        del self.arr[lastIdx]
                        lastIdx -= 1
                else:
                    self.arr[currIdx] = None
                break
            self.arr[currIdx] =  self.arr[minIdx]
            currIdx = minIdx

        return extracted

    # Find the index of the smaller child, or None if no children
    def find_min_idx(self, idx):
        c1 = 2 * idx + 1
        c2 = 2 * idx + 2
        N = len(self.arr)

        if c1 >= N and c2 >= N:
            return None
        elif c2 >= N:
            return c1
        elif self.arr[c1] == None:
            return c2
        elif self.arr[c2] == None:
            return c1
        else:
            if self.arr[c1] < self.arr[c2]:
                return c1
            else:
                return c2
            
    def clear(self):
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0
