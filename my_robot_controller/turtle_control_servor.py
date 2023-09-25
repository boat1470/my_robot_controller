#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
# /turtlesim/msg/Pose
from turtlesim.srv import SetPen
from functools import partial
class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller") # node name in graph
        self.get_logger().info("turtle_controller  start")
        self.cmd_vel_pub_=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.cmd_servo_=self.create_publisher(Twist,"/control/servo",10)  
        self.previous_x=0
        self.pose_subscriber_=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10) 
                                            #   msg type , topic , callback function ,size buffer
        
    
    def pose_callback(self,pose: Pose):
        cmd=Twist()
        if pose.x>9.0 or pose.x<2.0 or pose.y>9.0 or pose.y<2.0:
            cmd.linear.x=0.9
            cmd.angular.z=1.2
        else:
            cmd.linear.x=5.0
            cmd.angular.z=0.0

        self.cmd_vel_pub_.publish(cmd)

        # frequency in call service ,check condition befor set it
        if pose.x>5.5 and self.previous_x<=5.5:
            self.previous_x=pose.x
            self.get_logger().warn("set red")
            self.call_set_pen_service(255,0,0,3,0)
            cmd.linear.x=99.0
            self.cmd_servo_.publish(cmd)
        elif pose.x<=5.5 and self.previous_x>5.5:
            self.previous_x=pose.x
            self.get_logger().warn("set green")
            self.call_set_pen_service(0,255,0,3,0)
            cmd.linear.x=22.0
            self.cmd_servo_.publish(cmd)

    def call_set_pen_service(self,r,g,b,width,off):
        client=self.create_client(SetPen,"/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("wait for service . . .")

        request=SetPen.Request()
        request.r=r
        request.g=g
        request.b=b
        request.width=width
        request.off=off

        future=client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self,future):
        try: 
            response = future.result()

        except Exception as e:
            self.get_logger().error("service call faile: %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node=TurtleControllerNode()
    rclpy.spin(node) #continue to run   
    # enable all callback in Node
    rclpy.shutdown()
if __name__ == '__main__':
  main()
