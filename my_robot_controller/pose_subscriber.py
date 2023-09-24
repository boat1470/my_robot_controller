#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
# /turtlesim/msg/Pose

class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber") # node name in graph
        self.get_logger().info("draw circle start")

        self.pose_subscriber_=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10) 
                                            #   msg type , topic , callback function ,size buffer
        
    
    def pose_callback(self,msg:Pose):
        self.get_logger().info(str(msg.x))

def main(args=None):
    rclpy.init(args=args)
    node=PoseSubscriberNode()
    rclpy.spin(node) #continue to run   
    # enable all callback in Node
    rclpy.shutdown()
if __name__ == '__main__':
  main()
