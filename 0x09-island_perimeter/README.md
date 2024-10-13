# 0x09. Island Perimeter

## Tasks
### [0. Island Perimeter]()

Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

- [x] grid is a list of list of integers:
    - [x] 0 represents water
    - [x] 1 represents land
    - [x] Each cell is square, with a side length of 1
    - [x] Cells are connected horizontally/vertically (not diagonally).
    - [x] grid is rectangular, with its width and height not exceeding 100
- [x] The grid is completely surrounded by water
- [x] There is only one island (or nothing).
- [x] The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

```sh
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$ 
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$ 

```
Solution
Iterate through each cell in the grid.
For every cell that is 1 (land), check the four neighboring cells:
If the neighbor is out of bounds or is water (0), increment the perimeter by 1.
Return the total perimeter after processing all cells.
