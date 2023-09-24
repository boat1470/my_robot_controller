#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle") # node name in graph
        self.get_logger().info("draw 4circle start")

        self.cmd_vel_pub_=self.create_publisher(Twist,"/turtle1/cmd_vel",10) 
                                            #   msg type , topic ,size buffer
        
        self.timer_=self.create_timer(0.5,self.send_velocity_command)
    
    def send_velocity_command(self):
        msg=Twist()
        msg.linear.x=2.0
        msg.angular.z=1.0
        self.cmd_vel_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=DrawCircleNode()
    rclpy.spin(node) #continue to run   
    # enable all callback in Node
    rclpy.shutdown()
if __name__ == '__main__':
  main()
