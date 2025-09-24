class SortedList:
    def __init__(self):
        self.data = []

    def add(self, value):
        """Inserts `value` into the sorted list in \(O(\log n)\) time."""
        # Binary search to find the correct insertion position
        low, high = 0, len(self.data)
        while low < high:
            mid = (low + high) // 2
            if self.data[mid] < value:
                low = mid + 1
            else:
                high = mid
        
        # Inserting the value by shifting elements manually
        self.data.append(None)  # Increase the size of the list by 1
        for i in range(len(self.data) - 1, low, -1):
            self.data[i] = self.data[i - 1]
        self.data[low] = value

    def remove(self, value):
        """Removes `value` from the sorted list in \(O(\log n)\) time."""
        # Binary search to find the position of the value
        low, high = 0, len(self.data)
        while low < high:
            mid = (low + high) // 2
            if self.data[mid] < value:
                low = mid + 1
            else:
                high = mid

        # Remove the value by shifting elements manually
        if low < len(self.data) and self.data[low] == value:
            for i in range(low, len(self.data) - 1):
                self.data[i] = self.data[i + 1]
            self.data.pop()  # Remove the last element
        else:
            raise ValueError(f"{value} not in list")

    def bisect_left(self, value):
        """Finds the leftmost position for `value` in \(O(\log n)\) time."""
        low, high = 0, len(self.data)
        while low < high:
            mid = (low + high) // 2
            if self.data[mid] < value:
                low = mid + 1
            else:
                high = mid
        return low

    def bisect_right(self, value):
        """Finds the rightmost position for `value` in \(O(\log n)\) time."""
        low, high = 0, len(self.data)
        while low < high:
            mid = (low + high) // 2
            if self.data[mid] <= value:
                low = mid + 1
            else:
                high = mid
        return low

    def __getitem__(self, index):
        """Gets the element at the given index."""
        return self.data[index]

    def __len__(self):
        """Returns the number of elements in the sorted list."""
        return len(self.data)

    def __contains__(self, value):
        """Checks if `value` is in the sorted list."""
        # Binary search to check existence
        low, high = 0, len(self.data)
        while low < high:
            mid = (low + high) // 2
            if self.data[mid] < value:
                low = mid + 1
            elif self.data[mid] > value:
                high = mid
            else:
                return True
        return False



n , k = list(map(int , input().split()))
nums= list(map(int , input().split()))

res = []
heap = SortedList()
l = 0
for r in range(len(nums)):
    heap.add(nums[r])
    if r - l + 1 > k :
        heap.remove(nums[l])
        l += 1
    if r - l + 1 == k :
        res.append((heap[(k-1)//2]))

print(*res)