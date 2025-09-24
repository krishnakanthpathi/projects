from collections import defaultdict
from typing import List, Tuple, Set

def find(boxes: Set[Tuple[int, int]]) -> int:
    """
    Calculate the perimeter of all boxes using a more efficient approach.
    Each box contributes 4 to the perimeter unless it shares a side with another box.
    """
    total_perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x, y in boxes:
        for dx, dy in directions:
            if (x + dx, y + dy) not in boxes:
                total_perimeter += 1

    return total_perimeter


def main():
    n, m = map(int, input().split())  # Number of queries and size of each box
    tx, ty = 0, 0
    boxes = set()

    # Process queries and add box boundaries
    for _ in range(n):
        dx, dy = map(int, input().split())
        tx += dx
        ty += dy

        # Add only the perimeter cells of the box to reduce redundant computation
        for i in range(tx, tx + m):
            boxes.add((i, ty))  # Top edge
            boxes.add((i, ty + m - 1))  # Bottom edge
        for j in range(ty, ty + m):
            boxes.add((tx, j))  # Left edge
            boxes.add((tx + m - 1, j))  # Right edge

    # Calculate and print the perimeter
    print(find(boxes))


if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        main()
