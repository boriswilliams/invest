from typing import List

def isAllBool(arr: List[List[int]]) -> bool:
    for row in arr:
        for val in row:
            if not isinstance(val, bool):
                return False
    return True

def print2d(arr: List[List[int]], columnHeaders:List|int=None, rowHeaders:List|int=None) -> None:
    arr = [x[:] for x in arr]
    if isAllBool(arr):
        for row in arr:
            for i, x in enumerate(row):
                row[i] = 'X' if x else 'O'
    if rowHeaders:
        if isinstance(rowHeaders, int):
            rowHeaders = [x for x in range(rowHeaders)]
        for i in range(len(arr)):
            arr[i].insert(0, rowHeaders[i])
    if columnHeaders:
        if isinstance(columnHeaders, int):
            columnHeaders = [x for x in range(columnHeaders)]
        if rowHeaders:
            columnHeaders.insert(0, '')
        arr.insert(0, columnHeaders)
    colWidths = [0]*len(arr[0])
    for x in arr:
        for i, y in enumerate(x):
            colWidths[i] = max(colWidths[i], len(str(y)))
    for x in arr:
        for i, y in enumerate(x):
            print(str(y).rjust(colWidths[i]), end=' ')
        print()
    print()