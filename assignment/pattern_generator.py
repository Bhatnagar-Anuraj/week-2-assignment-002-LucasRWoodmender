import maya.cmds as cmds

cmds.file(new=True,force=True)


def generate_pattern():
   
#The informations on the 5 by 5 grid that is trying to be made with in the scene so I can use them in later things like range statments.
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
#This line puts cubes down on mutiples of 3. This only happens once in the scene since the second mutilple of three is 6 which the original if statement covers.
            elif (row + col) % 3 == 0:
                name = cmds.polyCube (name=box,width=width,height=height,depth=depth)[0]
#This changes the shape to a sphere if nither of the other statements happen. this allows for all shapes that should be made will be made.
            else:
                name = cmds.polySphere (name=box,radius=radius)[0]
            
# This allow for the different shapes to all move in the same way so that they all still make a 5 by 5 grid. 
            cmds.move(box_x,0,box_z,box)


generate_pattern()

cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
