# RescueAppForDBS
## CIIC 4060 / ICOM 5016 - Database Systems

Backend System for Disaster Rescue Resources Distribution System

### Usage:

A user (```users```) can be registered without specifying a role.

With one of the selections below, the type of user will be granted with the specific permissions.

  * A ```consumer``` can be added by specifying: first_name, last_name, address and phone.
    * By default, all consumers own the ```consumer_id```, and ```created_time``` based on the certain user_id. 
    * A consumer can update his/her Payment method and open a request and ask for the certain amount of resource. If the resource is free, he can reserve reserve it with no payment. If not free, the consumer needs to make an order and pay for the request.
  * A ```supplier``` can be added by specifying: suppier name, phone.
    * By default, a suppplier owns the ```supplier_id```, and ```created_time``` based on the certain user_id. 
    * A supplier suppliers some types of resouces, and a company will provide the product to a supplier. 
  * A system administrator (```administrator```) can be added by specifying: system administrator name.
    * The system administrator can be updated to specify which ```users``` are allowed to manage.
  
A ```company``` can be added by specifying the company's name. Company will not be able to provide ```resources```.

* To link a ```company``` to an existing ```supplier```, from ```supplier```, update ```supplier``` while providing the ```company``` ID.

A ```resource``` can be added by specifying the resource's name, type, price, location, and stock. A valid ```supplier``` needs to be specified for the ```resource``` to be available.

  * To generate a Google Maps Visual Indication, it will show based on address 
  
A ```reservation``` can be added by specifying the needed resource name, type, price, location, amount. A valid ```consumer``` and ```pay_method``` needs to be specified for a reservation to be valid.
 
  * Name, type, and price needs to match resource parameters.
    * The added action will return current time at that moment.
  
An ```order``` is only added if the requested item is not free.
    * The added new order will return current time at that moment.
    * Receives order number and time, and reference to an existing valid request.

A paying method (```pay_method```) can be added by specifying a payment method name and ```consumer``` ID. A valid ```consumer``` needs to be specified to have a valid payment method for the order;



### You need the following software installed to run this application:

1. PostgreSQL - database engine

2. Pyscopg2 - library to connect to PostgreSQL form Python

3. PgAdmin3 - app to manage the databases

4. Flask - web bases framework to implement the REST API.

5. Pycharm - python 3.5 
