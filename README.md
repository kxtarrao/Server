# Server
Server that queries a MongoDB database.

Instructions:

- Run database_setup.py
(This connects to database and writes test 
data)

- Run server.py to start server (Will run
  continuously)
  
- Enter python interactive mode on the
terminal and import client.py 
  
- Run methods in client.py

Example Command Set:

>from client import Client

>Client.start()

>Client.query("n10")

>Client.query("n6")

>Client.stop()
