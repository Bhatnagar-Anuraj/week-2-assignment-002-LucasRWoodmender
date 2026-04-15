"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================

OBJECTIVE:
    Use loops and conditionals to generate a repeating pattern of 3D objects
    in Maya. You will practice nested loops, conditional logic, and
    mathematical positioning.

REQUIREMENTS:
    1. Use a nested loop (a loop inside a loop) to create a grid or pattern
       of objects.
    2. Include at least one conditional (if/elif/else) that changes an
       object's properties (type, size, color, or position offset) based
       on its row, column, or index.
    3. Generate at least 25 objects total (e.g., a 5x5 grid).
    4. Comment every major block of code explaining your logic.

GRADING CRITERIA:
    - [25%] Nested loop correctly generates a grid/pattern of objects.
    - [25%] Conditional logic visibly changes object properties based on
            position or index.
    - [20%] At least 25 objects are generated.
    - [15%] Code is well-commented with clear explanations.
    - [15%] Pattern is visually interesting and intentional.

TIPS:
    - A 5x5 grid gives you 25 objects. A 6x6 grid gives you 36.
    - Use the loop variables (row, col) to calculate X and Z positions.
    - The modulo operator (%) is great for alternating patterns:
          if col % 2 == 0:    # every other column
    - You can vary: primitive type, height, width, position offset, etc.

COMMENT HABITS (practice these throughout the course):
    - Add a comment before each logical section explaining its purpose.
    - Use inline comments sparingly and only when the code is not obvious.
    - Keep comments up to date -- if you change the code, update the comment.
"""

import maya.cmds as cmds

# Clear the scene.

    """Generate a procedural pattern of objects using nested loops.

    This function should:
        1. Define variables for rows, columns, and spacing.
        2. Use a nested for-loop to iterate over rows and columns.
        3. Inside the loop, use a conditional to vary object properties.
        4. Create and position each object.
    """
    # --- Configuration variables ---
        # Distance between object centers.

    # TODO: Create a nested loop that iterates over rows and columns.
import maya.cmds as cmds

cmds.file(new=True, force=True)


def generate_pattern():    

#Give information to maya telling the amount of objectis in a row, how many rows, and the difference
#in position of each row. 
    num_rows = 5
    num_cols = 5
    spacing = 3.0
   
 #This line creates a 5 by 5 grid of boxs using the information from above. 
    for row in range(num_rows):
        for col in range(num_cols):
            box_x = col * spacing
            box_z = row * spacing
            box = f"Block_{row}_{col}"
            cmds.polyCube(name=box)
            cmds.move(box_x, 0, box_z, box)

#this tells maya to creat a cylinder if the rows + the cols ever equal 0 and if thats not the case
#to create a sphere.
            if (row + col) % 2 == 0:
                cmds.polyCylinder
            else:
                 cmds.polySphere
generate_pattern()

    
               
    
    #
    # HINT -- your loop structure should look something like this:
    #
    #   for row in range(num_rows):
    #       for col in range(num_cols):
    #           # Calculate position
    #           x_pos = col * spacing
    #           z_pos = row * spacing
    #
    #           # TODO: Add a conditional here that changes something
    #           # based on row, col, or (row + col).
    #           # For example:
    #           #   if (row + col) % 2 == 0:
    #           #       create a cube
    #           #   else:
    #           #       create a sphere
    
    #
    #           # TODO: Create the object using cmds.polyCube(), etc.
    #
    #           # TODO: Position the object using cmds.move().
    #
    #           # TODO: (Optional) Vary the scale using cmds.scale().




# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------


# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")fully!")
