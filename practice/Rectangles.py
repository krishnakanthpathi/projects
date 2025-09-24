import math
from collections import defaultdict

def main() :
    n , m = list(map(int , input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int , input().split())))
    row = defaultdict(defaultdict)
    col = defaultdict(defaultdict)

    for i in range(n):
        row[i] = {"b":0 , "w":0}
    for i in range(m):
        col[i] = {"b":0 , "w":0}

    for i in range(n):
        for j in range(m):
            row[i]["b"] += 1 if arr[i][j] == 1 else 0
            col[j]["b"] += 1 if arr[i][j] == 1 else 0
            row[i]["w"] += 1 if arr[i][j] == 0 else 0
            col[j]["w"] += 1 if arr[i][j] == 0 else 0
    res = 0
    for key in row :
        res += 2 ** row[key]["b"] - 1
        res += 2 ** row[key]["w"] - 1
    for key in col :
        res += 2 ** col[key]["b"] - 1
        res += 2 ** col[key]["w"] - 1
    print(res - m*n)
main()