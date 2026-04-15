import maya.cmds as cmds

cmds.file(new=True,force=True)


def generate_pattern():
   
#The informations on the 5 by 5 grid that is trying to be made with in the scene.
    num_rows = 5
    num_cols = 5
    spacing = 3.0
    
#information of the dimensions of the shapes.
    height = 2
    depth = 0.5
    radius = 1
    width = 0.5
#This line creates a 5 by 5 grid of boxs using the information from above. 
    for row in range(num_rows):
        for col in range(num_cols):
            box_x = col * spacing
            box_z = row * spacing
            box = f"block_{row}_{col}"
            
#These lines of code tell what shape should go where in the 5 by 5 grid.            
            if (row + col) % 2 == 0:
                name = cmds.polyCylinder (name=box,radius=radius, height=height)[0]
            elif (row + col) % 3 == 0:
                name = cmds.polyCube (name=box,width=width,height=height,depth=depth)[0]
            else:
                name = cmds.polySphere (name=box,radius=radius)[0]
            cmds.move(box_x,0,box_z,box)
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
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
