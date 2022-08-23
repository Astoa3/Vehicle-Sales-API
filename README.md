# Vehicle-Sales-API
Vehicle Sales inventory API. 

This application is an API based project for Vehicle Inventory. Users will be able
to search: Make, Model, Year, Color.

This project will utilize:

  Programming Language: Python
  
  API: OpenAPI Specification (SwaggerHub)
  
  Database: (Planned for MySQL, but was having issues with docker container. I created a database and did a few queries in the backend independent of API)
  
  Front-end and back-end code.
  
  Docker
  
  How to run:
  
  1. Download the vehicle_inventory folder
  2. Extract folder in a linux host
  3. Run CLI--> docker build --tag vehicle_inventory .
  4. Run CLI--> docker compose up
  5. This is the front-end link, this will display information of the Vehicle Sales inventory data gathered from API requests
  https://NMYS5F4YHJIRNU3S.anvil.app/6BNNJQMATJS4MAQ4TO4HBECI
  
  
  
  Notes: I haven't created an API, before and was confused on the endpoints and how to get the data that wasn't example data
  Example:
   http:APILink/inventory/{make}
   
   I had the properties set for
   
    make:
    description:
    
    Typed in Chevrolet to try and bring up an array of objects that contained Chevrolet as the make value, but would get the type that I set. The queries would just bring up property data.
    
    make: string
    description: string
    
    I have never played with building an API before though so it was interesting, my experience is mostly developing based on a created API like the ESRP.
    
    http://192.168.157.12:9000/inesrp/queues/{queueId}/prrs <--- My tool would databind all the queues in a specefied url and list them on the front end. A user from here would click enable and in the backend a put request would enable associated queue's prr, such as Time of Day. 
    
 I have a decent understanding building an API contextually, but would benefit off a few quick questions to verify some things. While I didn't utilize much of the mySQL database, I did create it via CLI and manipulate it via python script in the backend for practice over the weekend. I felt pretty comfortable building the Docker container as well, this project has got me pretty comfortable with that as well. 
  
