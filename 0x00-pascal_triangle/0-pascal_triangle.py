#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the last row in the triangle
        # Generate the current row
        row = [1]  # Start the row with a 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # End the row with a 1
        triangle.append(row)  # Add the current row to the triangle

    return triangle

