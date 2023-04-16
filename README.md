# Mastering-Web-3.0
Chosen language is python.

Made a class "Car" initialized with make,model and year.

speed is initialized to 0 for every car.

Direction and Coordinates are chosen randomly in the beggining.


Accelerate and Brake are self explanatory.

Movement method checks the direction and increments the coordinate in that direction, we do it modulo 10
(Since coordinates are integers, it creates an infinite 3-D lattice. But to make collisions more likely and easier to 
test I've made it finite with wraparound)

Time to collision method uses relative velocity to calculate how long it will take them to collide.
