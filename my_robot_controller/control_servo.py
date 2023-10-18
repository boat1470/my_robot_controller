#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
# /turtlesim/msg/Pose
from turtlesim.srv import SetPen
from functools import partial
#import RPi.GPIO as GPIO
import time
class ServoControllerNode(Node):
    def __init__(self):
        super().__init__("control_servo") # node name in graph
        self.get_logger().info("servo_controller  start99")    

       # GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(11,GPIO.OUT)
       # self.servo1=GPIO.PWM(11,50)

        self.pose_subscriber_=self.create_subscription(Twist,"/control/servo",self.servo_callback,10) 
                                            #   msg type , topic , callback function ,size buffer
        
    
    def servo_callback(self,data: Twist):
        # self.get_logger().info(data)
        #self.servo1.start(0)
        time.sleep(1)


        if data.linear.x==99.0 :
          #  duty= 180 /18+2
           # self.servo1.ChangeDutyCycle(duty)
            self.get_logger().info("180")
        elif data.linear.x==22.0 :
            #duty= 0 /18+2
            #self.servo1.ChangeDutyCycle(duty)
            self.get_logger().info("0")
        else:
            self.get_logger().info("what !!!!")

       # self.servo1.stop()
       # GPIO.cleanup()



def main(args=None):
    rclpy.init(args=args)
    node=ServoControllerNode()
    rclpy.spin(node) #continue to run   
    # enable all callback in Node
    rclpy.shutdown()
if __name__ == '__main__':
  main()
