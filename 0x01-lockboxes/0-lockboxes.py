#!/usr/bin/python3
"""lockboxes module"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be unlocked.

    Parameters
    ----------
    boxes : list of list of int
        A list where each element is a list of keys contained in the box.
    
    Returns
    -------
    bool
        True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)  # Total number of boxes
    unlocked = set([0])  # Start with the first box unlocked
    stack = [0]  # Stack to keep track of boxes to explore

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            # If the key corresponds to a box and it's not yet unlocked
            if key < n and key not in unlocked:
                unlocked.add(key)  # Unlock the box
                stack.append(key)  # Add the box to the stack to explore its keys

    # Check if the number of unlocked boxes equals the total number of boxes
    return len(unlocked) == n

