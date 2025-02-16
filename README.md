Lab 3 is a RESTful API Project built with FastAPI to manage a system that monitors the status of electronically measures water tanks. The API allows IOT enabled water tanks to report their volume and location, which can then be accessed and modified through HTTP requests.
This code was written to demonstrate the implementation of a RESTful API with a Create, Read, Update and Delete functionality. 

The functions used: 
GET/tank retreives the list of all water tanks in the system and also returns an empty list if no tanks have been added. 
GET/tank/{id} retreives the details of a specific tank using its unique ID. The function also returns a 404 error if thr tank is not found. 
POST/tank adds a new tank to the system, ensuring the required fields (location, lat, long) are in the request body. The function returns the created tank object with an automatically generated ID, and responds with a 201 status code on success.
PATCH/tank/{id} is used to update specific attributes of an existing tank and return the updated tank data or a 404 error if the tank is not found. 
DELETE/tank/{id} is used to remove a tank from the system using its unique ID, return a 204 status code on successful deletion or respond with a 404 error if the tank does not exist. 

TWO TRUTH ONE LIE:
I can cook a perfect three-course meal 
I can hold my breath for over two minutes 
I have never broken a bone
