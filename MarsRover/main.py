import os
from flask import Flask, request, render_template, jsonify, url_for


# Flask constructor
app = Flask(__name__)

# -------------------------------
# commands functions
# -------------------------------


# Move forward on current heading ,increase x
def Fcommand(x, y, Direction):
    X = x + 1
    return X, y, Direction


# B -> Move backwards on current heading ,decrease x
def Bcommand(x, y, Direction):
    X = x - 1
    return X, y, Direction


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


# -------------------------------
# handling browser caching
# -------------------------------
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/', methods=['GET'])
def index():
    #  render the Main page
    return render_template('index.html')


# which URL is associated function
@app.route('/mars', methods=["GET", "POST"])
def mars():
    if request.method == "POST":
        # getting input as json file
        data = request.get_json()

        # the command to move the rover
        command = data[0]["commands"]
        command=command.upper()
        # the initial positions for the rover
        position = data[1]["position"]

        # split the position into drection and x,y points
        data = position.split()
        direction = data[1]
        x, y = data[0].split(',')
        x, y = int(x), int(y)

        x, y, direction = Rover(command, x, y, direction)

        newResult = str(x) + "," + str(y) + " " + str(direction)

        # convert the results into json fromat before sending back to the API
        results = {'newResult': newResult}
        return jsonify(results)
    return None




if __name__ == '__main__':
    app.run()
