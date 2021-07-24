# Mars Rover
 A simple API using 
-  flask as backend (server side).
-  Html,CSS,javascript,Bootstarp as frontend(client side).


 
## Environment setup
 this code uses python 3.6.4 and Pycharm
- Good internet connection is required
- Install dependencies
```bash
$ pip install -r requirements.txt
```

### How to use the API
- run the main.py file in the python console

Note: all python calls below must be run from ./src
```bash
 main.py
```
- open the local serving address provided

>Running on http://127.0.0.1:5000/ 

- the address will direct to the main web page of the Mars Rover API
- The Mars Rover is initialized with Landing coordinates of (4,2) EAST 

![main-web-page](https://github.com/EbtihalSherif/Mars-Rover/blob/main/images/main%20web%20page.PNG)

- in the text input add your command to move the rover
- the updated position will be shown under the current position state

![moved-rover](https://raw.githubusercontent.com/EbtihalSherif/Mars-Rover/main/images/moved%20rover.PNG)

Note: as long the API is on , any request or command given to the API will take the last position and direction of the rover 






 
 
