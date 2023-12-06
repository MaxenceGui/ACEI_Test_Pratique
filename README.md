# ACEI_Test_Pratique
Technical test for interview with ACEI.

## Project
The project is a simple web site where you can send your data to a postgresql server and retrieve them. There is also three test that can be done on the server in the test.py folder.

### Structure
The project has three main component :
- The database which is a postgresql server
- The flask api with transit the data from the server to the database.
- The web site where the user can input and retrieve the data.

### Database
The database consist of a local postgresql server that has one table containing all the player added to the database.

### flask
The flask API has three main use. He can send data (a new player) to the database. He can ask for the full list of player in the database. Finally he can reset the list of player.

### Web site
The web site is essentially just a index.html file where the user can input the data and communicate with the database.

### To use
- To use this project, you will need to have a working postgresql environnement install, such as pgadmin. You can setup the database with your data in the CommunicationBD.py files.
- Also, a CORS blocker will be needed to let javascript communicate with Flask.

### Test
The test.py contains three functions to test directly the server.
- One of them create five new players
- One of them retrieve the players
- One of them reset the list 

