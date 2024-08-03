from controller import Robot
from controller import Motor
from controller import Altimeter
from controller import LED
import math


class MyController(Robot):
  def __init__(self):
    super(MyController,self).__init__()
    self.timeStep= 32
    
    self.altimeter= self.getDevice("altimeter")
    self.altimeter.enable(self.timeStep)
    
    self.left_motor= self.getDevice("left wheel motor")
    self.right_motor= self.getDevice("right wheel motor")
    self.left_motor.setPosition(math.inf)
    self.right_motor.setPosition(math.inf)
    
    self.direction_switch= False
    
  def run(self):
    while self.step(self.timeStep)!= -1:
      altitude= self.altimeter.getValue()
      if (not self.direction_switch):
        self.left_motor.setVelocity(2.0)
        self.right_motor.setVelocity(2.0)
        if(altitude<= 0.05):
          self.direction_switch= True
      else:
        self.left_motor.setVelocity(-2.0)
        self.right_motor.setVelocity(-2.0)
        
        if(altitude>= 0.25):
          self.direction_switch= False
          
controller= MyController()
controller.run()
         