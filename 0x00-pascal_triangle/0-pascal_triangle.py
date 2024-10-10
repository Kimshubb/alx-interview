#!/usr/bin/python3
"""pascal_triangle module
"""

def pascal_triangle(n):
    """Generate Pascal's triangle of size n.
    
    Parameters
    ----------
    n : int
        The number of rows in the Pascal's triangle to generate. Must be a non-negative integer.
    
    Returns
    -------
    list of list of int
        A list of lists, where each sublist represents a row in Pascal's triangle.
        Returns an empty list if n <= 0."""
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

