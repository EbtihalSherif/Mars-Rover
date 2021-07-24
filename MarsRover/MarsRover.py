
# -------------------------------
# commands functions
# -------------------------------

# Move forward on current heading ,increase x
def Fcommand(x, y, Direction):
    new_dir_dict = {
        'EAST': (x+1,y) ,
        'WEST': (x-1,y),
        'NORTH': (x,y+1),
        'SOUTH': (x,y-1)
    }
    X,Y=new_dir_dict.get(Direction)
  #  X = x + 1
    return X, Y, Direction


# B -> Move backwards on current heading ,decrease x
def Bcommand(x, y, Direction):
    new_dir_dict = {
        'EAST': (x - 1, y),
        'WEST': (x + 1, y),
        'NORTH': (x, y - 1),
        'SOUTH': (x, y + 1)
    }
    X, Y = new_dir_dict.get(Direction)
  #  X = x - 1
    return X, Y, Direction


# L -> rotate left from the current direction by 90 degrees
def Lcommand(x, y, Direction):
    # dictionary for the next rotation as it is constants
    # to avoid nested if conditions

    new_dir_dict = {
        'EAST': 'NORTH',
        'NORTH': 'WEST',
        'WEST': 'SOUTH',
        'SOUTH': 'EAST'
    }
    # get the new direction
    dir = new_dir_dict.get(Direction)
    return x, y, dir


# R -> rotate left from the current direction by 90 degrees
def Rcommand(x, y, Direction):
    # dictionary for the next rotation as it is constants
    # to avoid nested if conditions

    new_dir_dict = {
        'EAST': 'SOUTH',
        'SOUTH': 'WEST',
        'WEST': 'NORTH',
        'NORTH': 'EAST'
    }

    # get the new direction
    dir = new_dir_dict.get(Direction)
    return x, y, dir


# -------------------------------
# main function to loop over the rover commands
# -------------------------------
def Rover(command, x, y, Direction):

    # loop over the commands string to check each char
    for current in command:
        #check the current command to perform the right function
        if current == 'f' or current == 'F':
            x, y, Direction = Fcommand(x, y, Direction)
        elif current == 'b' or current == 'B':
            x, y, Direction , = Bcommand(x, y, Direction)
        elif current == 'l' or current == 'L':
            x, y, Direction = Lcommand(x, y, Direction)
        else:
            x, y, Direction = Rcommand(x, y, Direction)

    return x, y, Direction


