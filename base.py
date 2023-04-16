
import random




class Car :

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        #added movement direction because task was ambiguous
        self.direction = random.choice(["x","y","z"])
        self.x_coord = random.randint(1,9)
        self.y_coord = random.randint(1,9)
        self.z_coord = random.randint(1,9)

    def accelerate(self,speed_increment):
        self.speed += speed_increment
    
    def brake(self,speed_decrement):
        self.speed -= speed_decrement

    def move(self):
        if self.direction == "x" :
            self.x_coord += self.speed
            #Wrap around to make testing collisions easier
            self.x_coord = self.x_coord%10
        if self.direction == "y" :
            self.y_coord += self.speed
            #Wrap around to make testing collisions easier
            self.y_coord = self.y_coord%10
        if self.direction == "z" :
            self.z_coord += self.speed
            #Wrap around to make testing collisions easier
            self.z_coord = self.z_coord%10
    
    def detect_collision(self,car2):
        if self.x_coord == car2.x_coord and self.y_coord == car2.y_coord and self.z_coord == car2.z_coord :
            return True
        else :
            return False
        
    def time_to_collision(self,car2):
        if self.direction == car2.direction :
            if self.direction == "x" :
                return abs((self.x_coord - car2.x_coord)/(self.speed - car2.speed))
            if self.direction == "y" :
                return abs((self.y_coord - car2.y_coord)/(self.speed - car2.speed))
            if self.direction == "z" :
                return abs((self.z_coord - car2.z_coord)/(self.speed - car2.speed))
        else :
            return "Will Not Collide"   
        


car1 = Car("Test","Test",1923)
car2 = Car("Test","Test",1923)

car1.accelerate(5)
print(car1.speed)

car1.brake(3)
print(car1.speed)

car2.accelerate(1)

car1.move()
car2.move()

collision = car1.detect_collision(car2)
print(collision)

car1.move()
car2.move()

print(car1.time_to_collision(car2))




        
    
        
            





    
        