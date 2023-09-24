#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class Mynode(Node):
    def __init__(self):
        super().__init__("first_node99") # node name in graph
        self.get_logger().info("hello from Ros")
        self.create_timer(5.0,self.timer_callback)
    def timer_callback(self):
        self.get_logger().info("it time 5S")


def main(args=None):
    rclpy.init(args=args)
    node=Mynode()
    rclpy.spin(node) #continue to run   
    # enable all callback in Node
    rclpy.shutdown()
if __name__ == '__main__':
  main()
