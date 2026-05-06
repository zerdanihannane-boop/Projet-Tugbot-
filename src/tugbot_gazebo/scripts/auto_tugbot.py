#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class AutoTugbot(Node):
    def __init__(self):
        super().__init__('auto_tugbot')
        self.pub = self.create_publisher(Twist, '/model/tugbot/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move)

    def move(self):
        msg = Twist()
        msg.linear.x = 0.4
        msg.angular.z = 0.2
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = AutoTugbot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
