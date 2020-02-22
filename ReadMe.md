### Titanic Survival Prediction Application

The purpose of this application is to show competency in a few main areas:

- Python
- Machine Learning
- Django Web Application
- Docker

as such, this application uses the following technical stack:

- Python
- Machine Learning Stack
    - Numpy
    - Scikit Learn
    - Pandas
- Django
- Docker and Docker Compose

*Note: All information on the Machine Learning process used for this project can be found here: https://github.com/Matthew-Bowling/MachineLearning/tree/master/Titanic*

The structure of the web app is simple. There is an introductory page with a link to supply information on a general person. this persons data is then given to a machine learning algorithm which makes predictions. The predictions are shown on a following page as to whether they survived or not.

To run this application use the following commands:

`docker-compose build`

once the container has built:

`docker-compose up`

from here, our container is up and running our application having built the required python template with necessary packages. To access this application, per the `docker-compose.yml` just go to:

`localhost:8000`
