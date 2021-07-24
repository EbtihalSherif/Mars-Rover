import os
from flask import Flask, request, render_template, jsonify, url_for
from MarsRover import *
# Flask constructor
app = Flask(__name__)

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
