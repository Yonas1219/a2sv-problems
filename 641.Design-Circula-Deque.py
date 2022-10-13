class MyCircularDeque:
    def __init__(self, capacity: int):
        self.array = []
        self.size = capacity

    def insertFront(self, value: int) -> bool:
        if len(self.array) < self.size:
            self.array.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.array) < self.size:
            self.array.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.array) > 0:
            self.array.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.array) > 0:
            self.array.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.array) > 0:
            return self.array[0]
        return -1

    def getRear(self) -> int:
        if len(self.array) > 0:
            return self.array[-1]
        return -1

    def isEmpty(self) -> bool:
        if len(self.array) > 0:
            return False
        return True

    def isFull(self) -> bool:
        if len(self.array) == self.size:
            return True
        return False
