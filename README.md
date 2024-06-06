**Problem Statement**

Create an address book application where API users can create, update and delete addresses.

The address should:
  - contain the coordinates of the address.
  - be saved to an SQLite database.
  - be validated

API Users should also be able to retrieve the addresses that are within a given distance and location coordinates.

*Important : The application does not need a GUI. (Built-in FastAPI’s Swagger Doc is sufficient)*

-----
**Step by Step Solution**
-
-----
**_Note_:**

  **Latitude:**
  
  North: Positive values (0 to +90 degrees).
  
  South: Negative values (0 to -90 degrees).
  
  **Longitude:**
  
  East: Positive values (0 to +180 degrees).
  
  West: Negative values (0 to -180 degrees).

-----

1. Clone or download the repository on your machine

2. Create a virtual environment

    Creating virtual environment is important to ensure that all the necessary libraries can be installed there to run a specific project
  
       python -m venv <virtual_environment_name>

3. Activate virtual environment with the following command in the terminal

       <virtual_environment_name>\Scripts\activate   

4. Install all the dependencies from requirements.txt file

       pip install -r requirements.txt 

5. Go inside the app directory and execute FastAPI application - main.py

       uvicorn main:app

6. To Open Swagger application add "/docs" to the link and you can test the api's on swagger UI

   http://127.0.0.1:8000/docs

7. There are 5 apis for CRUD operations:

    1. Create Address
    2. Get Address By Distance
    3. Get All Addresses
    4. Delete Address
    5. Update Address
  
**To execute apis**

- Expand the api
- Click on Try it out to execute the api then provide the details
