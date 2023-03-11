# Live Bus Location For College Buses

### Implementation
----
1. Used ***Django-Channels*** to implement the socket connection betwwen Admin and Users
2. Used ***Redis*** for message queuing
3. In Front-End Used Javascript WebSockets to connect to a Socket
4. HTML & CSS for the UI
5. Used Django Models and ORM to add and store the details of Bus Routes, Stops etc

### There are 2 Sections Admin and User
----
* Admin Can Update The His Current Location
* Once Admin Updates The Current Location, It will be reflected in all the connected users without need of refreshing the web page.
