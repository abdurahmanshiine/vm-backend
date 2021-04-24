# Running the app with Makefile

To run the application on local machine in dev mode:

`make FLASK_ENV=Development dev`

To run the application on local machine in production mode:

`make FLASK_ENV=Production prod`

To run the dockerized version (which will build the image then run it locally):

`make`

The application will be run on port 8888 in all cases
